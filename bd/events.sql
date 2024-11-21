--eventos

SET GLOBAL event_scheduler = ON;

CREATE EVENT actualizar_pedidos_en_proceso
ON SCHEDULE EVERY 1 MINUTE
DO

UPDATE pedidos
SET estado_pedido = 'Completado'
WHERE estado_pedido = 'En proceso' 
  AND TIMESTAMPDIFF(MINUTE, fecha_pedido, NOW()) >= 60 AND estado_pedido != 'Cancelado';