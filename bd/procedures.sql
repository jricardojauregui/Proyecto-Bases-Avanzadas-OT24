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
CREATE PROCEDURE BorrarUsuario(
    IN p_id_usr INT
)
BEGIN
    DELETE FROM usuarios
    WHERE id_usr = p_id_usr;
END //
DELIMITER ;

-- Mostrar todos los usuarios

DELIMITER //
CREATE PROCEDURE MostrarTodosUsuarios()
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

--añadir producto a carrito

DELIMITER //

CREATE PROCEDURE anadirCarrito(
    IN p_id_usr INT,
    IN p_id_producto INT,
    IN p_cantidad INT
)
BEGIN
    INSERT INTO carrito_compras (id_usr, id_producto, cantidad, precio_unitario)
    SELECT p_id_usr, p_id_producto, p_cantidad, precio
    FROM productos
    WHERE id_producto = p_id_producto;
END //

DELIMITER ;

-- Mostrar productos por catgoria


DELIMITER //

CREATE PROCEDURE MostrarProductosPorNombreCategoria(
    IN p_nombre_categoria VARCHAR(100)
)
BEGIN
    SELECT p.foto_producto, p.nom_producto, p.precio
    FROM productos p INNER JOIN productos_categorias pc ON p.id_producto = pc.id_producto INNER JOIN categorias c ON pc.id_categoria = c.id_categoria WHERE c.categoria = p_nombre_categoria;
END //

DELIMITER ;


--mostrar productos mas nuevos (10)

DELIMITER //

CREATE PROCEDURE MostrarProductosMasNuevos()
BEGIN
    SELECT foto_producto, nom_producto, precio FROM productos ORDER BY fecha_agregacion DESC LIMIT 10;
END //

DELIMITER ;

--mostrar los 10 productos mas solicitados

DELIMITER //

DELIMITER //

CREATE PROCEDURE MostrarProductosMasSolicitadosParaWeb()
BEGIN
    SELECT p.foto_producto, p.nom_producto, p.precio FROM productos p INNER JOIN detalle_pedidos dp ON p.id_producto = dp.id_producto GROUP BY p.id_producto, p.foto_producto, p.nom_producto, p.precio ORDER BY SUM(dp.cantidad_solicitada) DESC LIMIT 10;
END //

DELIMITER ;


--actualizar stock

DELIMITER //

CREATE PROCEDURE ActualizarStock(
    IN p_id_producto INT,
    IN p_stock_agregado INT
)
BEGIN
    UPDATE inventario
    SET stock = stock + p_stock_agregado
    WHERE id_producto = p_id_producto;
END //

DELIMITER ;


--Mostrar carro compras

DELIMITER //

CREATE PROCEDURE MostrarCarritoDeUsuario(
    IN p_id_usr INT
)
BEGIN
    SELECT 
        c.id_producto, p.nom_producto, c.cantidad, c.precio_unitario, (c.cantidad * c.precio_unitario) AS total
    FROM 
        carrito_compras c INNER JOIN productos p ON c.id_producto = p.id_producto
    WHERE 
        c.id_usr = p_id_usr;
END //

DELIMITER ;

--Actualizar productos

DELIMITER //

CREATE PROCEDURE ActualizarProducto(
    IN p_id_producto INT,
    IN p_nom_producto VARCHAR(100),
    IN p_desc_producto TEXT,
    IN p_precio DECIMAL(10, 2),
    IN p_empresa_nom VARCHAR(100)
)
BEGIN
    UPDATE productos
    SET 
        nom_producto = p_nom_producto,
        desc_producto = p_desc_producto,
        precio = p_precio,
        empresa_nom = p_empresa_nom
    WHERE 
        id_producto = p_id_producto;
END //

DELIMITER ;


--Mostrar productos en promocion

DELIMITER //

CREATE PROCEDURE MostrarProductosEnPromocion()
BEGIN
    SELECT p.id_producto, p.nom_producto, p.desc_producto, p.precio, pr.nom_promocion, pr.descuento, pr.fecha_inicio, pr.fecha_fin FROM productos p INNER JOIN productos_promociones pp ON p.id_producto = pp.id_producto INNER JOIN promociones pr ON pp.id_promocion = pr.id_promocion WHERE pr.activo = TRUE ORDER BY pr.fecha_fin ASC;
END //

DELIMITER ;


--historial de pedidos por usuario

DELIMITER //

CREATE PROCEDURE HistorialPedidosPorUsuario(
    IN p_id_usr INT
)
BEGIN
    SELECT p.id_pedido, p.fecha_pedido, p.estado_pedido, dp.id_producto, prod.nom_producto, dp.cantidad_solicitada, dp.precio_unitario, dp.subtotal
    FROM pedidos p INNER JOIN detalle_pedidos dp ON p.id_pedido = dp.id_pedido INNER JOIN productos prod ON dp.id_producto = prod.id_producto WHERE p.id_usr = p_id_usr ORDER BY p.fecha_pedido DESC;
END //

DELIMITER ;


--Instertar productos

DELIMITER //

CREATE PROCEDURE InsertarProducto(
    IN p_nom_producto VARCHAR(100),
    IN p_desc_producto TEXT,
    IN p_precio DECIMAL(10, 2),
    IN p_empresa_nom VARCHAR(100),
    IN p_foto_producto VARCHAR(255)
)
BEGIN
    INSERT INTO productos (
        nom_producto, desc_producto, precio, empresa_nom, foto_producto
    )
    VALUES (
        p_nom_producto, p_desc_producto, p_precio, p_empresa_nom, p_foto_producto
    );
END //

DELIMITER ;

-- borrar productos

DELIMITER //

CREATE PROCEDURE BorrarProducto(
    IN p_id_producto INT
)
BEGIN
    DELETE FROM productos
    WHERE id_producto = p_id_producto;
END //

DELIMITER ;

--asignar categoria a productos

DELIMITER //

CREATE PROCEDURE AsignarCategoriaAProducto(
    IN p_id_categoria INT,
    IN p_id_producto INT
)
BEGIN
    IF NOT EXISTS (
        SELECT 1 
        FROM productos_categorias 
        WHERE id_categoria = p_id_categoria AND id_producto = p_id_producto
    ) THEN
        INSERT INTO productos_categorias (id_categoria, id_producto)
        VALUES (p_id_categoria, p_id_producto);
    ELSE
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'La categoría ya está asignada al producto.';
    END IF;
END //

DELIMITER ;


--crear promocion

DELIMITER //

CREATE PROCEDURE InsertarPromocion(
    IN p_nom_promocion VARCHAR(100),
    IN p_descuento DECIMAL(5, 2),
    IN p_fecha_inicio DATE,
    IN p_fecha_fin DATE,
    IN p_activo BOOLEAN
)
BEGIN
    INSERT INTO promociones (
        nom_promocion, descuento, fecha_inicio, fecha_fin, activo
    )
    VALUES (
        p_nom_promocion, p_descuento, p_fecha_inicio, p_fecha_fin, p_activo
    );
END //

DELIMITER ;


--editar promocion

DELIMITER //

CREATE PROCEDURE EditarPromocion(
    IN p_id_promocion INT,
    IN p_nom_promocion VARCHAR(100),
    IN p_descuento DECIMAL(5, 2),
    IN p_fecha_inicio DATE,
    IN p_fecha_fin DATE,
    IN p_activo BOOLEAN
)
BEGIN
    UPDATE promociones
    SET 
        nom_promocion = p_nom_promocion,
        descuento = p_descuento,
        fecha_inicio = p_fecha_inicio,
        fecha_fin = p_fecha_fin,
        activo = p_activo
    WHERE 
        id_promocion = p_id_promocion;
END //

DELIMITER ;


--borrar promocion

DELIMITER //

CREATE PROCEDURE BorrarPromocion(
    IN p_id_promocion INT
)
BEGIN
    DELETE FROM promociones
    WHERE id_promocion = p_id_promocion;
END //

DELIMITER ;

--asignar promocion a productos

DELIMITER //

CREATE PROCEDURE AsignarPromocionAProducto(
    IN p_id_promocion INT,
    IN p_id_producto INT
)
BEGIN
    INSERT INTO productos_promociones (id_promocion, id_producto)
    VALUES (p_id_promocion, p_id_producto);
END //

DELIMITER ;

--desasignar promociones a productos

DELIMITER //
CREATE PROCEDURE DesasignarPromocionProducto(
    IN p_id_promocion INT,
    IN p_id_producto INT
)
BEGIN
    DELETE FROM productos_promociones
    WHERE id_promocion = p_id_promocion AND id_producto = p_id_producto;
END //
DELIMITER ;


-- mostrar producto en especifico

DELIMITER //
CREATE PROCEDURE MostrarProductoEspecifico(
    IN p_id_producto INT
)
BEGIN
    SELECT id_producto, nom_producto, desc_producto, precio, empresa_nom, fecha_agregacion, foto_producto FROM productos WHERE id_producto = p_id_producto;
END //
DELIMITER ;



--añadir producto a wish list

DELIMITER //
CREATE PROCEDURE AnadirProductoWishList(
    IN p_id_usr INT,
    IN p_id_producto INT
)
BEGIN
    INSERT INTO wish_list (id_usr, id_producto, fecha_agregado) VALUES (p_id_usr, p_id_producto, CURRENT_TIMESTAMP);
END //
DELIMITER ;


-- quitar producto a wish list

DELIMITER //
CREATE PROCEDURE QuitarProductoWishList(
    IN p_id_usr INT,
    IN p_id_producto INT
)
BEGIN
    DELETE FROM wish_list WHERE id_usr = p_id_usr AND id_producto = p_id_producto;
END //
DELIMITER ;



-- quitar del carrito (individual)

DELIMITER //
CREATE PROCEDURE QuitarProductoCarrito(
    IN p_id_usr INT,
    IN p_id_producto INT
)
BEGIN
    DELETE FROM carrito_compras WHERE id_usr = p_id_usr AND id_producto = p_id_producto;
END //
DELIMITER ;

-- quitar del carrito todo

DELIMITER //
CREATE PROCEDURE QuitarTodoCarrito(
    IN p_id_usr INT
)
BEGIN
    DELETE FROM carrito_compras WHERE id_usr = p_id_usr;
END //
DELIMITER ;

--añadir tarjeta

DELIMITER //

CREATE PROCEDURE AnadirTarjeta(
    IN p_id_usr INT,
    IN p_tarjeta_usr VARCHAR(100),
    IN p_id_banco INT,
    IN p_propietario VARCHAR(100),
    IN p_caduci_tarjeta VARCHAR(100)
)
BEGIN
    INSERT INTO tarjetas (id_usr, tarjeta_usr, id_banco, propietario, caduci_tarjeta) VALUES (p_id_usr, p_tarjeta_usr, p_id_banco, p_propietario, p_caduci_tarjeta);
END //

DELIMITER ;

--borrar tarjeta

DELIMITER //

CREATE PROCEDURE BorrarTarjeta(
    IN p_id_usr INT,
    IN p_tarjeta_usr VARCHAR(100)
)
BEGIN
    DECLARE v_tarjetas_count INT;
    SELECT COUNT(*) INTO v_tarjetas_count FROM tarjetas WHERE id_usr = p_id_usr;
    IF v_tarjetas_count > 1 THEN
        DELETE FROM tarjetas
        WHERE id_usr = p_id_usr AND tarjeta_usr = p_tarjeta_usr;
    ELSE
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Tienes que tener una tarjeta registrada.';
    END IF;
END //

DELIMITER ;


--sistema de recomendaciones

DELIMITER //
CREATE PROCEDURE sistemaRecomendaciones(
    IN p_id_usr INT
)
BEGIN
    DECLARE p_id_categoria INT;
    SELECT pc.id_categoria INTO p_id_categoria FROM detalle_pedidos dp INNER JOIN productos p ON dp.id_producto = p.id_producto INNER JOIN productos_categorias pc ON p.id_producto = pc.id_producto WHERE dp.id_pedido IN (SELECT id_pedido FROM pedidos WHERE id_usr = p_id_usr) GROUP BY pc.id_categoria ORDER BY COUNT(*) DESC LIMIT 1;

    SELECT p.foto_producto, p.nom_producto, p.precio FROM productos p INNER JOIN productos_categorias pc ON p.id_producto = pc.id_producto WHERE pc.id_categoria = p_id_categoria ORDER BY p.fecha_agregacion DESC LIMIT 5;
END //
DELIMITER ;

--crear calificaciones por producto

DELIMITER //
CREATE PROCEDURE CrearCalificacion(
    IN p_id_usr INT,
    IN p_id_producto INT,
    IN p_calificacion INT,
    IN p_comentario TEXT
)
BEGIN
    INSERT INTO calificaciones (id_usr, id_producto, calificacion, comentario) VALUES (p_id_usr, p_id_producto, p_calificacion, p_comentario);
END //
DELIMITER ;


-- borrar calificaciones por producto

DELIMITER //
CREATE PROCEDURE BorrarCalificacion(
    IN p_id_calificacion INT
)
BEGIN
    DELETE FROM calificaciones WHERE id_calificacion = p_id_calificacion;
END //
DELIMITER ;


-- ver calificaciones por producto

DELIMITER //
CREATE PROCEDURE VerCalificacionesPorProducto(
    IN p_id_producto INT
)
BEGIN
    SELECT id_calificacion, id_usr, calificacion, comentario, fecha_calificacion FROM calificaciones WHERE id_producto = p_id_producto;
END //
DELIMITER ;

--ver tarjetas usuario

DELIMITER //

CREATE PROCEDURE verTarjetasUsuario(
    IN p_id_usr INT
)
BEGIN 
    SELECT tarjeta_usr, banco_usr FROM tarjetas t INNER JOIN bancos b ON t.id_banco = b.id_banco WHERE t.id_usr = p_id_usr;
END //

DELIMITER ;


--crear categorias

DELIMITER //
CREATE PROCEDURE CrearCategoria(
    IN p_nombre_categoria VARCHAR(100),
    IN p_desc_categoria TEXT
)
BEGIN
    INSERT INTO categorias (categoria, desc_categorias) VALUES (p_nombre_categoria, p_desc_categoria);
END //
DELIMITER ;

--borrar categorias

DELIMITER //
CREATE PROCEDURE BorrarCategoria(
    IN p_id_categoria INT
)
BEGIN
    DELETE FROM categorias WHERE id_categoria = p_id_categoria;
END //

DELIMITER ;

-- mostrar wishlist

DELIMITER //

CREATE PROCEDURE MostrarWishList(
    IN p_id_usr INT
)
BEGIN
    SELECT wl.id_producto, p.nom_producto, p.desc_producto, p.precio, p.empresa_nom FROM wish_list wl INNER JOIN productos p ON wl.id_producto = p.id_producto WHERE wl.id_usr = p_id_usr;
END //

DELIMITER ;

-- cancelar pedido

DELIMITER //

CREATE PROCEDURE CancelarPedido(
    IN p_id_pedido INT
)
BEGIN
    DECLARE p_estado_pedido VARCHAR(50);
    SELECT estado_pedido INTO p_estado_pedido FROM pedidos WHERE id_pedido = p_id_pedido;
    IF p_estado_pedido = 'En proceso' THEN
        UPDATE pedidos SET estado_pedido = 'Cancelado' WHERE id_pedido = p_id_pedido;
    ELSE
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El pedido no se puede cancelar porque ya se entrego.';
    END IF;
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE VerificarUsuario(
    IN p_id_usr INT
)
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM usuarios
        WHERE id_usr = p_id_usr
    ) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'El usuario no existe.';
    END IF;
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE ToggleProductoWishList(
    IN id_usr INT,
    IN id_producto INT
)
BEGIN
    DECLARE existe INT;

    SELECT COUNT(*) INTO existe
    FROM wish_list
    WHERE id_usr = id_usr AND id_producto = id_producto;

    IF existe > 0 THEN
        DELETE FROM wish_list
        WHERE id_usr = id_usr AND id_producto = id_producto;
    ELSE
        INSERT INTO wish_list (id_usr, id_producto)
        VALUES (id_usr, id_producto);
    END IF;
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE UltimaCompra(
    IN id_usr INT,
    IN id_producto INT
)
BEGIN
    SELECT MAX(p.fecha_pedido) AS last_purchase_date
    FROM pedidos p
    INNER JOIN detalle_pedidos dp ON p.id_pedido = dp.id_pedido
    WHERE p.id_usr = id_usr 
      AND dp.id_producto = id_producto 
      AND p.estado_pedido != 'Cancelado';
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE productoCategoria(
    IN id_producto INT
)
BEGIN
    SELECT c.categoria
    FROM productos p
    INNER JOIN productos_categorias pc ON p.id_producto = pc.id_producto
    INNER JOIN categorias c ON pc.id_categoria = c.id_categoria
    WHERE p.id_producto = id_producto;
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE checarWishlist(
    IN id_usr INT,
    IN id_producto INT
)
BEGIN
    SELECT 1 
    FROM wish_list 
    WHERE id_usr = id_usr AND id_producto = id_producto;
END //

DELIMITER ;


DELIMITER //

CREATE PROCEDURE autenticarUser(
    IN username VARCHAR(255),
    IN hashed_password VARCHAR(255)
)
BEGIN
    SELECT id_usr 
    FROM usuarios 
    WHERE username = username AND clave = hashed_password;
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE todosProductos()
BEGIN
    SELECT 
        id_producto, 
        nom_producto, 
        precio, 
        foto_producto 
    FROM productos;
END //

DELIMITER ;

DELIMITER //
CREATE PROCEDURE productosPorCategoria(
    IN p_id_categoria INT
)
BEGIN
    SELECT 
        p.id_producto, p.nom_producto, p.precio, p.foto_producto
    FROM 
        productos p
    INNER JOIN 
        productos_categorias pc ON p.id_producto = pc.id_producto
    WHERE 
        pc.id_categoria = p_id_categoria;
END //
DELIMITER ;

--grafico de promedio de calificaciones

DELIMITER //

CREATE PROCEDURE promedioCalifProductos()
BEGIN
    SELECT nom_producto, COALESCE(promedio_calificacion, 0) AS promedio_calificacion FROM CalificacionesPromedioPorProducto;
END //

DELIMITER ;

--cant de productos por categorias


DELIMITER //

CREATE PROCEDURE cantProductosCategorias()
BEGIN
    SELECT categoria, cantidad_productos FROM CategoriasCantidadPorductos;
END //

DELIMITER ;


--Cant de stock por producto

DELIMITER //

CREATE PROCEDURE cantProductosStock()
BEGIN
    SELECT producto, cantidad_stock FROM VistaProductosStock;
END //

DELIMITER ;



--pedidos por mes

DELIMITER //

CREATE PROCEDURE pedidosPorMes()
BEGIN
    SELECT mes, total_pedidos from PedidosPorMes;
END //

DELIMITER ;


--Usuarios por mes

DELIMITER //

CREATE PROCEDURE UsuariosPorMes()
BEGIN
    SELECT mes, usuarios_activos from usuariosPorMes;
END //

DELIMITER ;

--pedidos cancelados

DELIMITER //

CREATE PROCEDURE verCancelados()
BEGIN
    SELECT count(*) AS Total FROM PedidosCancelados;
END //

DELIMITER ;

-- pedidos en proceso

DELIMITER //

CREATE PROCEDURE verCompletados()
BEGIN
    SELECT count(*) AS Total FROM PedidosCompletos;
END //

DELIMITER ;

--pedidos completados

DELIMITER //

CREATE PROCEDURE verEnProceso()
BEGIN
    SELECT count(*) AS Total FROM PedidosEnProceso;
END //

DELIMITER ;

--Ganacias por mes


DELIMITER //

CREATE PROCEDURE gananciasPorMes()
BEGIN
    SELECT mes, ganancias from GananciasPorMes;
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE VerificarRolAdmin(
    IN p_id_usr INT
)
BEGIN
    SELECT 1
    FROM usuarios_roles ur
    INNER JOIN roles r ON ur.id_rol = r.id_rol
    WHERE ur.id_usr = p_id_usr AND r.nom_rol = 'Administrador';
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE ActualizarCampoUsuario(
    IN p_id_usr INT,
    IN p_campo VARCHAR(100),
    IN p_valor TEXT
)
BEGIN
    SET @query = CONCAT('UPDATE usuarios SET ', p_campo, ' = ? WHERE id_usr = ?');
    PREPARE stmt FROM @query;
    EXECUTE stmt USING p_valor, p_id_usr;
    DEALLOCATE PREPARE stmt;
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE MostrarTodasOrdenes()
BEGIN
    SELECT 
        p.id_pedido, p.fecha_pedido, p.estado_pedido, u.username, u.nom_usr, u.apellido_usr, t.tarjeta_usr
    FROM pedidos p
    INNER JOIN usuarios u ON p.id_usr = u.id_usr
    INNER JOIN tarjetas t ON p.tarjeta_usr = t.tarjeta_usr;
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE ActualizarEstadoOrden(
    IN p_id_pedido INT,
    IN p_estado_pedido VARCHAR(50)
)
BEGIN
    UPDATE pedidos
    SET estado_pedido = p_estado_pedido
    WHERE id_pedido = p_id_pedido;
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE BorrarOrden(
    IN p_id_pedido INT
)
BEGIN
    DELETE FROM pedidos
    WHERE id_pedido = p_id_pedido;
END //

DELIMITER ;

DELIMITER //
CREATE PROCEDURE sistemaRecomendaciones(
    IN p_id_usr INT
)
BEGIN
    DECLARE p_id_categoria INT;
    SELECT pc.id_categoria INTO p_id_categoria FROM detalle_pedidos dp INNER JOIN productos p ON dp.id_producto = p.id_producto INNER JOIN productos_categorias pc ON p.id_producto = pc.id_producto WHERE dp.id_pedido IN (SELECT id_pedido FROM pedidos WHERE id_usr = p_id_usr) GROUP BY pc.id_categoria ORDER BY COUNT(*) DESC LIMIT 1;

    SELECT p.foto_producto, p.nom_producto, p.precio FROM productos p INNER JOIN productos_categorias pc ON p.id_producto = pc.id_producto WHERE pc.id_categoria = p_id_categoria ORDER BY p.fecha_agregacion DESC LIMIT 5;
END //
DELIMITER ;