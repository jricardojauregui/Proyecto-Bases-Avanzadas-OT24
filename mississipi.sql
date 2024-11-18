CREATE TABLE usuarios (
    id_usr INT NOT NULL PRIMARY KEY AUTO_INCREMENT, 
    nom_usr VARCHAR(100) NOT NULL,
    apellido_usr VARCHAR(100) NOT NULL,
    correo_usr VARCHAR(100) NOT NULL,
    tel_usr VARCHAR(100) NOT NULL,
    tel_domicilio VARCHAR(100) NOT NULL,
    direccion VARCHAR(100) NOT NULL,
    fecha_registro DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE bancos (
    id_banco INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    banco_usr VARCHAR(100) NOT NULL
);

CREATE TABLE tarjetas (
    id_usr INT NOT NULL,
    tarjeta_usr VARCHAR(100) NOT NULL,  
    id_banco INT NOT NULL,
    propietario VARCHAR(100) NOT NULL,  
    caduci_tarjeta VARCHAR(100) NOT NULL,
    PRIMARY KEY (tarjeta_usr, id_usr),
    FOREIGN KEY (id_usr) REFERENCES usuarios(id_usr),
    FOREIGN KEY (id_banco) REFERENCES bancos(id_banco)
);

CREATE TABLE categorias (
    id_categoria INT NOT NULL AUTO_INCREMENT,
    categoria VARCHAR(100) NOT NULL,
    desc_categorias VARCHAR(100) NOT NULL,
    PRIMARY KEY (id_categoria)
);

CREATE TABLE productos (
    id_producto INT NOT NULL AUTO_INCREMENT,
    nom_producto VARCHAR(100) NOT NULL,
    desc_producto TEXT NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    fecha_agregacion DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    empresa_nom VARCHAR(100) NOT NULL,
    PRIMARY KEY (id_producto)
);

CREATE TABLE productos_categorias (
    id_categoria INT NOT NULL,
    id_producto INT NOT NULL,
    PRIMARY KEY (id_categoria, id_producto),
    FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria),
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
);

CREATE TABLE pedidos (
    id_pedido INT NOT NULL AUTO_INCREMENT,
    fecha_pedido DATE NOT NULL,
    estado_pedido VARCHAR(50) NOT NULL,
    id_usr INT NOT NULL,
    tarjeta_usr VARCHAR(100) NOT NULL, 
    PRIMARY KEY (id_pedido),
    FOREIGN KEY (id_usr, tarjeta_usr) REFERENCES tarjetas(id_usr, tarjeta_usr)
);

CREATE TABLE inventario (
    id_inventario INT NOT NULL AUTO_INCREMENT,
    id_producto INT NOT NULL,
    stock INT NOT NULL,
    ultima_actualizacion DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id_inventario),
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
);

CREATE TABLE detalle_pedidos (
    id_detalle INT NOT NULL AUTO_INCREMENT,
    id_pedido INT NOT NULL,
    id_producto INT NOT NULL,
    cantidad_solicitada INT NOT NULL,
    precio_unitario DECIMAL(10, 2) NOT NULL,
    subtotal DECIMAL(10, 2) GENERATED ALWAYS AS (cantidad_solicitada * precio_unitario) STORED,
    PRIMARY KEY (id_detalle),
    FOREIGN KEY (id_pedido) REFERENCES pedidos(id_pedido),
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
);