--inserta usuario

DELIMITER //
CREATE PROCEDURE InsertUsuario(
    IN p_username VARCHAR(100),
    IN p_clave VARCHAR(100),
    IN p_nom_usr VARCHAR(100),
    IN p_apellido_usr VARCHAR(100),
    IN p_correo_usr VARCHAR(100),
    IN p_tel_usr VARCHAR(100),
    IN p_tel_domicilio VARCHAR(100),
    IN p_direccion VARCHAR(100),
    IN p_foto_usuario VARCHAR(255)
)
BEGIN
    INSERT INTO usuarios (
        username, clave, nom_usr, apellido_usr, correo_usr, tel_usr, tel_domicilio, direccion, foto_usuario
    ) 
    VALUES (
        p_username, p_clave, p_nom_usr, p_apellido_usr, p_correo_usr, p_tel_usr, p_tel_domicilio, p_direccion, p_foto_usuario
    );
END //
DELIMITER ;

-- Actualizar un usuario 

DELIMITER //
CREATE PROCEDURE UpdateUsuario(
    IN p_username VARCHAR(100),
    IN p_clave VARCHAR(100),
    IN p_nom_usr VARCHAR(100),
    IN p_apellido_usr VARCHAR(100),
    IN p_correo_usr VARCHAR(100),
    IN p_tel_usr VARCHAR(100),
    IN p_tel_domicilio VARCHAR(100),
    IN p_direccion VARCHAR(100),
    IN p_foto_usuario VARCHAR(255)
)
BEGIN
    UPDATE usuarios
    SET 
        username = p_username,
        clave = p_clave,
        nom_usr = p_nom_usr,
        apellido_usr = p_apellido_usr,
        correo_usr = p_correo_usr,
        tel_usr = p_tel_usr,
        tel_domicilio = p_tel_domicilio,
        direccion = p_direccion,
        foto_usuario = p_foto_usuario
    WHERE 
        id_usr = p_id_usr;
END //
DELIMITER ;

-- delete usuario

DELIMITER //
CREATE PROCEDURE DeleteUsuario(
    IN p_id_usr INT
)
BEGIN
    DELETE FROM usuarios
    WHERE id_usr = p_id_usr;
END //
DELIMITER ;

-- Mostrar todos los usuarios

DELIMITER //
CREATE PROCEDURE MostrarUsuarios()
BEGIN
    SELECT 
        id_usr, clave, nom_usr, apellido_usr, correo_usr, tel_usr, tel_domicilio, direccion, fecha_registro, foto_usuario
    FROM 
        usuarios;
END //
DELIMITER ;

-- Mostrar un usuario por ID

DELIMITER //
CREATE PROCEDURE MostrarUsuarioPorID(
    IN p_id_usr INT
)
BEGIN
    SELECT 
        id_usr, clave, nom_usr, apellido_usr, correo_usr, tel_usr, tel_domicilio, direccion, fecha_registro, foto_usuario
    FROM 
        usuarios
    WHERE 
        id_usr = p_id_usr;
END //
DELIMITER ;


DELIMITER //
CREATE PROCEDURE MostrarUsuarioPorID(
    IN p_nombre_usr INT
)
BEGIN
    SELECT 
        id_usr, clave, nom_usr, apellido_usr, correo_usr, tel_usr, tel_domicilio, direccion, fecha_registro, foto_usuario
    FROM 
        usuarios
    WHERE 
        nom_usr = p_nombre_usr;
END //
DELIMITER ;


--confirma compra en carrito

DELIMITER //
CREATE PROCEDURE ConfirmarCompra(IN p_id_usr INT, IN p_tarjeta_usr VARCHAR(100))
BEGIN
    DECLARE v_id_pedido INT;
    INSERT INTO pedidos (fecha_pedido, estado_pedido, id_usr, tarjeta_usr)
    VALUES (CURDATE(), 'Completado', p_id_usr, p_tarjeta_usr);
    SET v_id_pedido = LAST_INSERT_ID();
    INSERT INTO detalle_pedidos (id_pedido, id_producto, cantidad_solicitada, precio_unitario)
    SELECT v_id_pedido, id_producto, cantidad, precio_unitario
    FROM carrito_compras
    WHERE id_usr = p_id_usr;
    UPDATE inventario i
    INNER JOIN carrito_compras c ON i.id_producto = c.id_producto
    SET i.stock = i.stock - c.cantidad
    WHERE c.id_usr = p_id_usr;
    DELETE FROM carrito_compras WHERE id_usr = p_id_usr;
END //
DELIMITER ;


-- procedimiento para comprar sin carrito 

DELIMITER //

CREATE PROCEDURE CompraDirecta(
    IN p_id_usr INT,
    IN p_id_producto INT,
    IN p_cantidad INT,
    IN p_tarjeta_usr VARCHAR(100)
)
BEGIN
    DECLARE v_id_pedido INT;
    INSERT INTO pedidos (fecha_pedido, id_usr, tarjeta_usr)
    VALUES (CURDATE(), p_id_usr, p_tarjeta_usr);
    SET v_id_pedido = LAST_INSERT_ID();

    INSERT INTO detalle_pedidos (id_pedido, id_producto, cantidad_solicitada, precio_unitario)
    VALUES (v_id_pedido, p_id_producto, p_cantidad, (SELECT precio FROM productos WHERE id_producto = p_id_producto));
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE anadirCarrito(
    IN p_id_usr INT,
    IN p_id_producto INT,
    IN p_cantidad INT
)
BEGIN
    INSERT INTO carrito_compras (id_usr, id_producto, cantidad, precio_unitario) SELECT p_id_usr, p_id_producto p_cantidad, precio FROM productos WHERE id_producto = p_id_producto;
END //

DELIMITER ;



