--vista para ver productos sin stock

CREATE VIEW ProductosSinStock AS SELECT p.id_producto, p.nom_producto, p.empresa_nom, i.stock FROM productos p INNER JOIN inventario i ON p.id_producto = i.id_producto WHERE i.stock = 0;

--mostrar promociones activas

CREATE VIEW PromocionesActivas AS SELECT id_promocion, nom_promocion, descuento, fecha_inicio, fecha_fin
FROM promociones WHERE activo = TRUE;



--mostrar Categorías con Cantidad de Productos

CREATE VIEW CategoriasCantidadPorductos AS SELECT c.id_categoria, c.categoria, COUNT(pc.id_producto) AS cantidad_productos FROM categorias c LEFT JOIN productos_categorias pc ON c.id_categoria = pc.id_categoria GROUP BY c.id_categoria, c.categoria;



--una vista para Pedidos Completados


CREATE VIEW PedidosCompletos AS SELECT p.id_pedido, p.fecha_pedido, p.id_usr, u.nom_usr, u.apellido_usr, SUM(dp.cantidad_solicitada * dp.precio_unitario) AS total_pedido FROM pedidos p INNER JOIN detalle_pedidos dp ON p.id_pedido = dp.id_pedido INNER JOIN usuarios u ON p.id_usr = u.id_usr WHERE p.estado_pedido = 'Completado' GROUP BY p.id_pedido, p.fecha_pedido, p.id_usr, u.nom_usr, u.apellido_usr;


--vista de pedidos Cancelados

CREATE VIEW PedidosCancelados AS SELECT p.id_pedido, p.fecha_pedido, p.id_usr, u.nom_usr, u.apellido_usr, SUM(dp.cantidad_solicitada * dp.precio_unitario) AS total_pedido FROM pedidos p INNER JOIN detalle_pedidos dp ON p.id_pedido = dp.id_pedido INNER JOIN usuarios u ON p.id_usr = u.id_usr WHERE p.estado_pedido = 'Cancelado' GROUP BY p.id_pedido, p.fecha_pedido, p.id_usr, u.nom_usr, u.apellido_usr;

--vista de pedidos pendientes

CREATE VIEW PedidosEnProceso AS SELECT p.id_pedido, p.fecha_pedido, p.id_usr, u.nom_usr, u.apellido_usr, SUM(dp.cantidad_solicitada * dp.precio_unitario) AS total_pedido FROM pedidos p INNER JOIN detalle_pedidos dp ON p.id_pedido = dp.id_pedido INNER JOIN usuarios u ON p.id_usr = u.id_usr WHERE p.estado_pedido = 'En proceso' GROUP BY p.id_pedido, p.fecha_pedido, p.id_usr, u.nom_usr, u.apellido_usr;

--una vista para Productos con Promociones


CREATE VIEW ProductosConPromociones AS SELECT p.id_producto, p.nom_producto, p.precio, pr.nom_promocion, pr.descuento, pr.fecha_fin FROM  productos p INNER JOIN productos_promociones pp ON p.id_producto = pp.id_producto INNER JOIN promociones pr ON pp.id_promocion = pr.id_promocion WHERE pr.activo = TRUE;

--una vista de Calificaciones Promedio por Producto

CREATE VIEW CalificacionesPromedioPorProducto AS SELECT p.id_producto, p.nom_producto, AVG(c.calificacion) AS promedio_calificacion, COUNT(c.id_calificacion) AS total_calificaciones FROM productos p LEFT JOIN calificaciones c ON p.id_producto = c.id_producto GROUP BY p.id_producto, p.nom_producto;


--productos stock

CREATE VIEW VistaProductosStock AS SELECT p.nom_producto AS producto, i.stock AS cantidad_stock FROM productos p INNER JOIN inventario i ON p.id_producto = i.id_producto;

--vista de pedidos por mes

CREATE VIEW PedidosPorMes AS SELECT DATE_FORMAT(fecha_pedido, '%Y-%m') AS mes, COUNT(*) AS total_pedidos FROM pedidos GROUP BY mes ORDER BY mes;

--usuarios activos por mes

CREATE VIEW usuariosPorMes AS SELECT DATE_FORMAT(fecha_pedido, '%Y-%m') AS mes, COUNT(DISTINCT id_usr) AS usuarios_activos FROM pedidos GROUP BY mes ORDER BY mes;

--ganacias por mes

CREATE VIEW GananciasPorMes AS SELECT DATE_FORMAT(p.fecha_pedido, '%Y-%m') AS mes, SUM(dp.cantidad_solicitada * dp.precio_unitario) AS ganancias FROM pedidos p INNER JOIN detalle_pedidos dp ON p.id_pedido = dp.id_pedido WHERE p. estado_pedido = 'Completado' OR estado_pedido = 'En proceso' GROUP BY DATE_FORMAT(p.fecha_pedido, '%Y-%m') ORDER BY mes ASC;
