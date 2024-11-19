INSERT INTO usuarios (clave, nom_usr, apellido_usr, correo_usr, tel_usr, tel_domicilio, direccion, foto_usuario)
VALUES 
('clave123!', 'Juan', 'Pérez', 'juan.perez@gmail.com', '1234567890', '0987654321', 'Calle 123, Monterrey'),
('maria456$', 'María', 'González', 'maria.gonzalez@hotmail.com', '2233445567', '6655443328', 'Calle 456, Guadalajara'),
('carlos789#', 'Carlos', 'López', 'carlos.lopez@outlook.com', '9988776659', '5566778891', 'Calle 789, CDMX'),
('ana654$', 'Ana', 'Martínez', 'ana.martinez@gmail.com', '1122334466', '5544332299', 'Calle 321, Puebla'),
('luis321*', 'Luis', 'Ramírez', 'luis.ramirez@yahoo.com', '4433221112', '1100223355', 'Calle 654, León'),
('elena789&', 'Elena', 'Sánchez', 'elena.sanchez@hotmail.com', '6677889902', '0099887767', 'Calle 987, Querétaro'),
('pablo123^', 'Pablo', 'Hernández', 'pablo.hernandez@gmail.com', '9988772235', '2233441123', 'Calle 852, Mérida'),
('lucia456!', 'Lucía', 'Castro', 'lucia.castro@outlook.com', '3344556688', '7766554435', 'Calle 741, Cancún'),
('diego789$', 'Diego', 'Morales', 'diego.morales@gmail.com', '5566778811', '9988776666', 'Calle 963, Tijuana'),
('fer159!', 'Fernanda', 'Ortega', 'fernanda.ortega@yahoo.com', '6655443344', '2233445577', 'Calle 159, Saltillo'),
('gabriel753#', 'Gabriel', 'Núñez', 'gabriel.nunez@outlook.com', '1122334477', '5544332233', 'Calle 753, Oaxaca'),
('paola951$', 'Paola', 'Mendoza', 'paola.mendoza@gmail.com', '4433221144', '1100223388', 'Calle 951, Veracruz'),
('manuel951&', 'Manuel', 'Reyes', 'manuel.reyes@hotmail.com', '3344556679', '7766554436', 'Calle 951, Chihuahua'),
('alejandra753^', 'Alejandra', 'Vega', 'alejandra.vega@outlook.com', '5566778844', '2233441199', 'Calle 753, Mexicali'),
('sofia741*', 'Sofía', 'Torres', 'sofia.torres@gmail.com', '2233445599', '6655443399', 'Calle 741, Aguascalientes'),
('sebastian852$', 'Sebastián', 'Flores', 'sebastian.flores@hotmail.com', '1122334488', '5544332277', 'Calle 852, Morelia'),
('isabel963!', 'Isabel', 'Cruz', 'isabel.cruz@outlook.com', '4433221199', '1100223344', 'Calle 963, Ensenada'),
('daniel159^', 'Daniel', 'Vargas', 'daniel.vargas@gmail.com', '3344556699', '7766554455', 'Calle 159, Zacatecas'),
('andrea951#', 'Andrea', 'Ríos', 'andrea.rios@hotmail.com', '5566778855', '2233441133', 'Calle 951, Villahermosa'),
('miguel753$', 'Miguel', 'Estrada', 'miguel.estrada@gmail.com', '9988776677', '6655443377', 'Calle 753, San Luis Potosí'),
('javier123!', 'Javier', 'Domínguez', 'javier.dominguez@gmail.com', '3322114455', '5544331177', 'Calle 852, Tijuana'),
('natalia456$', 'Natalia', 'Fernández', 'natalia.fernandez@hotmail.com', '7766554433', '6655443311', 'Calle 963, Guadalajara'),
('ricardo789#', 'Ricardo', 'Guzmán', 'ricardo.guzman@outlook.com', '2233445566', '5544332266', 'Calle 741, CDMX'),
('claudia654$', 'Claudia', 'Navarro', 'claudia.navarro@gmail.com', '3344556677', '2233441177', 'Calle 159, Puebla'),
('hector321*', 'Héctor', 'Suárez', 'hector.suarez@yahoo.com', '5566778899', '1122334455', 'Calle 753, León'),
('veronica789&', 'Verónica', 'Ruiz', 'veronica.ruiz@hotmail.com', '6677889900', '5544332233', 'Calle 456, Querétaro'),
('roberto123^', 'Roberto', 'Jiménez', 'roberto.jimenez@gmail.com', '9988776655', '3344556677', 'Calle 654, Mérida'),
('karina456!', 'Karina', 'Silva', 'karina.silva@outlook.com', '1122334456', '2233445588', 'Calle 852, Cancún'),
('jorge789$', 'Jorge', 'Aguilar', 'jorge.aguilar@gmail.com', '9988772233', '5544331199', 'Calle 753, Saltillo'),
('carmen654$', 'Carmen', 'Santos', 'carmen.santos@hotmail.com', '6677889901', '2233441155', 'Calle 963, Oaxaca');


INSERT INTO bancos (banco_usr)
VALUES 
('BBVA'), 
('Santander'), 
('Banorte'), 
('HSBC'), 
('Citibanamex'),
('Scotiabank'),
('Inbursa'),
('Banco Azteca'),
('Banco del Bienestar'),
('Banregio');

INSERT INTO tarjetas (id_usr, tarjeta_usr, id_banco, propietario, caduci_tarjeta)
VALUES 
(1, '4111111111111111', 1, 'Juan Pérez', '12/25'),
(1, '4222222222222222', 2, 'Juan Pérez', '05/26'),
(2, '4333333333333333', 3, 'María González', '07/24'),
(3, '4444444444444444', 4, 'Carlos López', '09/27'),
(4, '4555555555555555', 5, 'Ana Martínez', '11/23'),
(5, '4666666666666666', 6, 'Luis Ramírez', '02/28'),
(6, '4777777777777777', 7, 'Elena Sánchez', '04/29'),
(7, '4888888888888888', 8, 'Pablo Hernández', '01/27'),
(8, '4999999999999999', 9, 'Lucía Castro', '08/30'),
(9, '4000000000000000', 10, 'Diego Morales', '03/25'),
(10, '4111222233334444', 1, 'Fernanda Ortega', '12/24'),
(11, '4222333344445555', 2, 'Gabriel Núñez', '06/26'),
(12, '4333444455556666', 3, 'Paola Mendoza', '10/28'),
(13, '4444555566667777', 4, 'Manuel Reyes', '01/29'),
(14, '4555666677778888', 5, 'Alejandra Vega', '05/24'),
(15, '4666777788889999', 6, 'Sofía Torres', '02/27'),
(16, '4777888899990000', 7, 'Sebastián Flores', '09/26'),
(17, '4888999900001111', 8, 'Isabel Cruz', '07/25'),
(18, '4999000011112222', 9, 'Daniel Vargas', '03/24'),
(19, '4000111122223333', 10, 'Andrea Ríos', '08/30'),
(21, '5000000000001111', 2, 'Javier Domínguez', '05/27'),
(22, '5000000000003333', 4, 'Natalia Fernández', '03/28'),
(22, '5000000000004444', 5, 'Natalia Fernández', '08/25'),
(23, '5000000000005555', 6, 'Ricardo Guzmán', '07/27'),
(24, '5000000000006666', 1, 'Claudia Navarro', '01/29'),
(25, '5000000000007777', 9, 'Héctor Suárez', '12/30'),
(26, '5000000000008888', 8, 'Verónica Ruiz', '06/26'),
(27, '5000000000009999', 7, 'Roberto Jiménez', '09/27'),
(28, '5000000000010000', 6, 'Karina Silva', '02/29'),
(29, '5000000000011111', 2, 'Jorge Aguilar', '11/28'),
(30, '5000000000012222', 3, 'Carmen Santos', '04/30');

INSERT INTO productos (nom_producto, desc_producto, precio, empresa_nom)
VALUES 
('Smartphone Samsung Galaxy S21', 'Teléfono móvil de gama alta con pantalla de 6.2 pulgadas', 21999.99, 'Samsung'),
('Laptop Dell XPS 13', 'Ultrabook de 13 pulgadas con Intel Core i7 y 16GB RAM', 39999.99, 'Dell'),
('Televisión LG OLED55C1', 'Televisor OLED de 55 pulgadas con resolución 4K', 31999.99, 'LG'),
('Audífonos Sony WH-1000XM4', 'Audífonos inalámbricos con cancelación de ruido', 7999.99, 'Sony'),
('Reloj Inteligente Apple Watch Series 7', 'Reloj inteligente con múltiples funciones de salud', 9999.99, 'Apple'),
('Camiseta Deportiva Nike', 'Camiseta de algodón para entrenamiento', 399.99, 'Nike'),
('Balón de Fútbol Adidas', 'Balón de fútbol oficial tamaño 5', 799.99, 'Adidas'),
('Bicicleta de Montaña Trek Marlin 7', 'Bicicleta de montaña con suspensión delantera', 15999.99, 'Trek'),
('Horno de Microondas Panasonic', 'Microondas de 1200W con capacidad de 30 litros', 4499.99, 'Panasonic'),
('Refrigerador Whirlpool WRX735SDHZ', 'Refrigerador de 3 puertas con dispensador de agua', 49999.99, 'Whirlpool'),
('Drone DJI Mavic Air 2', 'Drone con cámara 4K y estabilizador', 19999.99, 'DJI'),
('Licuadora Oster Pro', 'Licuadora de alta potencia con vaso de vidrio', 2999.99, 'Oster'),
('Cafetera Nespresso Vertuo', 'Cafetera automática para cápsulas', 6999.99, 'Nespresso'),
('Sofá Seccional de Tela', 'Sofá seccional con capacidad para 5 personas', 17999.99, 'IKEA'),
('Lámpara de Escritorio Philips', 'Lámpara LED ajustable para escritorio', 1299.99, 'Philips'),
('Teclado Mecánico Logitech G Pro', 'Teclado mecánico para gamers', 2499.99, 'Logitech'),
('Silla de Oficina Ergonomía Steelcase', 'Silla de oficina ergonómica de alta calidad', 19999.99, 'Steelcase'),
('Set de Ollas T-Fal', 'Juego de ollas antiadherentes de 10 piezas', 4999.99, 'T-Fal'),
('Cámara Fotográfica Canon EOS R5', 'Cámara mirrorless de alta resolución', 99999.99, 'Canon'),
('iPad Pro 12.9"', 'Tableta de alto rendimiento con pantalla de 12.9 pulgadas', 34999.99, 'Apple'),
('Smartwatch Garmin Fenix 6', 'Reloj deportivo premium con GPS', 17999.99, 'Garmin'),
('Router TP-Link AX6000', 'Router Wi-Fi 6 de alto rendimiento', 5999.99, 'TP-Link'),
('Lavadora LG TurboWash', 'Lavadora automática de 20kg con vapor', 15999.99, 'LG'),
('Cámara de Seguridad Arlo Pro 4', 'Cámara de seguridad inalámbrica con resolución 2K', 7999.99, 'Arlo'),
('iPhone 14 Pro Max', 'Teléfono móvil con pantalla de 6.7 pulgadas y cámaras avanzadas', 33999.99, 'Apple'),
('Consola PlayStation 5', 'Consola de videojuegos de última generación', 13999.99, 'Sony'),
('Xbox Series X', 'Consola de videojuegos de alta gama', 13499.99, 'Microsoft'),
('Tablet Amazon Fire HD 10', 'Tablet económica con pantalla de 10 pulgadas', 3999.99, 'Amazon'),
('Juego de Comedor para 6 Personas', 'Comedor moderno de madera', 15999.99, 'IKEA'),
('Colchón Memory Foam Sealy', 'Colchón tamaño Queen con espuma de memoria', 19999.99, 'Sealy');


INSERT INTO productos_categorias (id_categoria, id_producto)
VALUES 
(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), 
(3, 6), (3, 7), 
(5, 8), (2, 9), (2, 10), 
(4, 11), (2, 12), 
(4, 13), (2, 14), 
(1, 15), (5, 16),
(5, 17), (2, 18), 
(1, 19), (1, 20), 
(5, 21), (1, 22), 
(2, 23), (4, 24),
(1, 25), (4, 26),
(1, 27), (1, 28), 
(2, 29), (2, 30);

INSERT INTO pedidos (fecha_pedido, estado_pedido, id_usr, tarjeta_usr)
VALUES

('2024-01-10', 'Completado', 1, '4111111111111111'),
('2024-01-12', 'Pendiente', 2, '4333333333333333'),
('2024-01-15', 'En Proceso', 3, '4444444444444444'),
('2024-01-18', 'Completado', 4, '4555555555555555'),
('2024-01-20', 'Cancelado', 5, '4666666666666666'),
('2024-01-25', 'Completado', 6, '4777777777777777'),
('2024-01-30', 'En Proceso', 7, '4888888888888888'),
('2024-02-02', 'Pendiente', 8, '4999999999999999'),
('2024-02-05', 'Completado', 9, '4000000000000000'),
('2024-02-10', 'Completado', 10, '4111222233334444'),
('2024-02-15', 'Pendiente', 11, '4222333344445555'),
('2024-02-20', 'Completado', 12, '4333444455556666'),
('2024-02-25', 'En Proceso', 13, '4444555566667777'),
('2024-02-28', 'Completado', 14, '4555666677778888'),
('2024-03-01', 'Pendiente', 15, '4666777788889999'),
('2024-03-05', 'En Proceso', 16, '4777888899990000'),
('2024-03-10', 'Completado', 17, '4888999900001111'),
('2024-03-15', 'Pendiente', 18, '4999000011112222'),
('2024-03-20', 'Completado', 19, '4000111122223333'),
('2024-03-25', 'Pendiente', 20, '4111222233334444'),
('2024-03-30', 'Completado', 21, '5000000000001111'),
('2024-04-05', 'En Proceso', 22, '5000000000002222'),
('2024-04-10', 'Pendiente', 23, '5000000000003333'),
('2024-04-15', 'Completado', 24, '5000000000004444'),
('2024-04-20', 'Pendiente', 25, '5000000000005555'),
('2024-04-25', 'Completado', 26, '5000000000006666'),
('2024-04-30', 'Pendiente', 27, '5000000000007777'),
('2024-05-05', 'Completado', 28, '5000000000008888'),
('2024-05-10', 'Pendiente', 29, '5000000000009999'),
('2024-05-15', 'Completado', 30, '5000000000010000');


INSERT INTO detalle_pedidos (id_pedido, id_producto, cantidad_solicitada, precio_unitario)
VALUES
(1, 1, 1, 21999.99), (1, 3, 1, 31999.99), (1, 5, 2, 9999.99),
(2, 6, 2, 399.99), (2, 7, 1, 799.99), (2, 8, 1, 15999.99),
(3, 9, 1, 4499.99), (3, 10, 1, 49999.99), (3, 11, 1, 19999.99),
(4, 12, 1, 6999.99), (4, 13, 1, 17999.99), (4, 14, 1, 17999.99),
(5, 15, 2, 1299.99), (5, 16, 1, 2499.99), (5, 17, 1, 19999.99),
(6, 18, 1, 4999.99), (6, 19, 1, 99999.99), (6, 20, 1, 34999.99),
(7, 21, 1, 5999.99), (7, 22, 1, 13499.99), (7, 23, 1, 15999.99),
(8, 24, 1, 7999.99), (8, 25, 1, 15999.99),
(9, 26, 1, 13499.99), (9, 27, 1, 9999.99),
(10, 28, 1, 3999.99),
(11, 29, 1, 9999.99),
(12, 30, 1, 3999.99),
(13, 1, 1, 21999.99),
(14, 2, 1, 39999.99),
(15, 3, 1, 31999.99),
(16, 4, 1, 7999.99),
(17, 5, 1, 9999.99),
(18, 6, 2, 399.99),
(19, 7, 1, 799.99),
(20, 8, 1, 15999.99),
(21, 9, 1, 4499.99),
(22, 10, 1, 49999.99),
(23, 11, 1, 19999.99),
(24, 12, 1, 6999.99),
(25, 13, 1, 17999.99),
(26, 14, 1, 17999.99),
(27, 15, 1, 1299.99),
(28, 16, 1, 2499.99),
(29, 17, 1, 19999.99),
(30, 18, 1, 4999.99);