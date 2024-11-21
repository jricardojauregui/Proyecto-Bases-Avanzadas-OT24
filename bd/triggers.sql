-- triggers y procedures

DELIMITER //

CREATE TRIGGER vaciar_carrito
AFTER INSERT ON pedidos
FOR EACH ROW
BEGIN
    DELETE FROM carrito_compras WHERE id_usr = NEW.id_usr;
END //

DELIMITER ;

--sha9 a claves

DELIMITER //

CREATE TRIGGER before_insert_hash_clave
BEFORE INSERT ON usuarios
FOR EACH ROW
BEGIN
    SET NEW.clave = SHA2(NEW.clave, 256);
END //

DELIMITER ;

-- actualizar inventario con stock

DELIMITER //

CREATE TRIGGER actualizar_inventario
AFTER INSERT ON detalle_pedidos
FOR EACH ROW
BEGIN
    UPDATE inventario
    SET stock = stock - NEW.cantidad_solicitada
    WHERE id_producto = NEW.id_producto;
END //

DELIMITER ;

-- revisar stock antes de compras

DELIMITER //

CREATE TRIGGER validar_stock_carrito
BEFORE INSERT ON carrito_compras
FOR EACH ROW
BEGIN
    DECLARE stock_actual INT;
    SELECT stock INTO stock_actual
    FROM inventario
    WHERE id_producto = NEW.id_producto;
    IF stock_actual < NEW.cantidad THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'No hay cantidad suficiente para agregar al carrito.';
    END IF;
END //

DELIMITER ;

--automatizar registros en historial de compras

DELIMITER //

CREATE TRIGGER registrar_historial_compras
AFTER UPDATE ON pedidos
FOR EACH ROW
BEGIN
    IF NEW.estado_pedido = 'Completado' THEN
        INSERT INTO historial_compras (id_usr, id_producto, fecha_compra)
        SELECT NEW.id_usr, dp.id_producto, NOW()
        FROM detalle_pedidos dp
        WHERE dp.id_pedido = NEW.id_pedido;
    END IF;
END //

DELIMITER ;

--no borrar usuarios con pedidos activos

DELIMITER //

CREATE TRIGGER validar_eliminacion_usuario
BEFORE DELETE ON usuarios
FOR EACH ROW
BEGIN
    IF EXISTS (
        SELECT 1
        FROM pedidos
        WHERE id_usr = OLD.id_usr AND estado_pedido IN ('Pendiente', 'En Proceso')
    ) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'No se puede eliminar el usuario porque tiene pedidos activos.';
    END IF;
END //

DELIMITER ;


--restablecer inventario en caso de que cancelen

DELIMITER //
CREATE TRIGGER reabastecer_inventario
AFTER UPDATE ON pedidos
FOR EACH ROW
BEGIN
    IF NEW.estado_pedido = 'Cancelado' THEN
        UPDATE inventario i
        INNER JOIN detalle_pedidos dp ON i.id_producto = dp.id_producto
        SET i.stock = i.stock + dp.cantidad_solicitada
        WHERE dp.id_pedido = NEW.id_pedido;
    END IF;
END //
DELIMITER ;


--actualizar fecha inventario

DELIMITER //
CREATE TRIGGER actualizar_fecha_inventario
BEFORE UPDATE ON inventario
FOR EACH ROW
BEGIN
    SET NEW.ultima_actualizacion = CURRENT_TIMESTAMP;
END //
DELIMITER ;


--asignar precio al pedido (congelado)

DELIMITER //
CREATE TRIGGER fijar_precio_unitario
BEFORE INSERT ON detalle_pedidos
FOR EACH ROW
BEGIN
    DECLARE v_precio DECIMAL(10, 2);
    SELECT precio INTO v_precio FROM productos WHERE id_producto = NEW.id_producto;
    SET NEW.precio_unitario = v_precio;
END //
DELIMITER ;

--revisar duplicidad en el carrito

DELIMITER //
CREATE TRIGGER validar_producto_carrito
BEFORE INSERT ON carrito_compras
FOR EACH ROW
BEGIN
    IF EXISTS (
        SELECT 1 FROM carrito_compras
        WHERE id_usr = NEW.id_usr AND id_producto = NEW.id_producto
    ) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'El producto ya está en el carrito.';
    END IF;
END //
DELIMITER ;

--asignar usuario directamente a clientes

DELIMITER //
CREATE TRIGGER asignar_rol_cliente
AFTER INSERT ON usuarios
FOR EACH ROW
BEGIN
    INSERT INTO usuarios_roles (id_usr, id_rol)
    VALUES (NEW.id_usr, (SELECT id_rol FROM roles WHERE nom_rol = 'Cliente'));
END //
DELIMITER ;

