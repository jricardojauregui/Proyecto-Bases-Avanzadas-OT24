-- Tabla de Usuarios
CREATE TABLE usuarios (
    id_usr INT NOT NULL PRIMARY KEY AUTO_INCREMENT, 
    username varchar(100) NOT NULL,
    clave VARCHAR(100) NOT NULL,
    nom_usr VARCHAR(100) NOT NULL,
    apellido_usr VARCHAR(100) NOT NULL,
    correo_usr VARCHAR(100) NOT NULL,
    tel_usr VARCHAR(100) NOT NULL UNIQUE,
    tel_domicilio VARCHAR(100) NOT NULL,
    direccion VARCHAR(100) NOT NULL,
    fecha_registro DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    foto_usuario VARCHAR(255)
);

-- Tabla de Bancos
CREATE TABLE bancos (
    id_banco INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    banco_usr VARCHAR(100) NOT NULL
);

-- Tabla de Tarjetas
CREATE TABLE tarjetas (
    id_usr INT NOT NULL,
    tarjeta_usr VARCHAR(100) NOT NULL UNIQUE,  
    id_banco INT NOT NULL,
    propietario VARCHAR(100) NOT NULL,  
    caduci_tarjeta VARCHAR(100) NOT NULL,
    PRIMARY KEY (tarjeta_usr, id_usr),
    FOREIGN KEY (id_usr) REFERENCES usuarios(id_usr),
    FOREIGN KEY (id_banco) REFERENCES bancos(id_banco)
);

-- Tabla de Categorías
CREATE TABLE categorias (
    id_categoria INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    categoria VARCHAR(100) NOT NULL,
    desc_categorias VARCHAR(100) NOT NULL
);

-- Tabla de Productos
CREATE TABLE productos (
    id_producto INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nom_producto VARCHAR(100) NOT NULL,
    desc_producto TEXT NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    fecha_agregacion DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    empresa_nom VARCHAR(100) NOT NULL,
    foto_producto VARCHAR(255)
);

-- Relación entre Productos y Categorías
CREATE TABLE productos_categorias (
    id_categoria INT NOT NULL,
    id_producto INT NOT NULL,
    PRIMARY KEY (id_categoria, id_producto),
    FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria),
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
);

-- Tabla de Pedidos
CREATE TABLE pedidos (
    id_pedido INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    fecha_pedido DATE NOT NULL,
    estado_pedido VARCHAR(50) NOT NULL,
    id_usr INT NOT NULL,
    tarjeta_usr VARCHAR(100) NOT NULL, 
    FOREIGN KEY (id_usr, tarjeta_usr) REFERENCES tarjetas(id_usr, tarjeta_usr)
);

-- Detalle de Pedidos
CREATE TABLE detalle_pedidos (
    id_detalle INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    id_pedido INT NOT NULL,
    id_producto INT NOT NULL,
    cantidad_solicitada INT NOT NULL,
    precio_unitario DECIMAL(10, 2) NOT NULL,
    subtotal DECIMAL(10, 2) GENERATED ALWAYS AS (cantidad_solicitada * precio_unitario) STORED,
    FOREIGN KEY (id_pedido) REFERENCES pedidos(id_pedido),
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
);

-- Tabla de Inventario
CREATE TABLE inventario (
    id_inventario INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    id_producto INT NOT NULL,
    stock INT NOT NULL,
    ultima_actualizacion DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
);

-- Carrito de Compras
CREATE TABLE carrito_compras (
    id_carrito INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    id_usr INT NOT NULL,
    id_producto INT NOT NULL,
    cantidad INT NOT NULL DEFAULT 1,
    precio_unitario DECIMAL(10, 2) NOT NULL,
    fecha_agregado DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_usr) REFERENCES usuarios(id_usr),
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
);

-- Lista de Deseos (Wishlist)
CREATE TABLE wish_list (
    id_wish_list INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    id_usr INT NOT NULL,
    id_producto INT NOT NULL,
    fecha_agregado DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_usr) REFERENCES usuarios(id_usr),
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
);

-- Tabla de Calificaciones
CREATE TABLE calificaciones (
    id_calificacion INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    id_usr INT NOT NULL,
    id_producto INT NOT NULL,
    calificacion INT NOT NULL CHECK (calificacion BETWEEN 1 AND 5),
    comentario TEXT,
    fecha_calificacion DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_usr) REFERENCES usuarios(id_usr),
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
);

-- Tabla de Promociones
CREATE TABLE promociones (
    id_promocion INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nom_promocion VARCHAR(100) NOT NULL,
    descuento DECIMAL(5, 2) NOT NULL, -- Porcentaje de descuento
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE NOT NULL,
    activo BOOLEAN NOT NULL DEFAULT TRUE
);

-- Relación entre Productos y Promociones
CREATE TABLE productos_promociones (
    id_promocion INT NOT NULL,
    id_producto INT NOT NULL,
    PRIMARY KEY (id_promocion, id_producto),
    FOREIGN KEY (id_promocion) REFERENCES promociones(id_promocion),
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
);

-- Tabla de Roles
CREATE TABLE roles (
    id_rol INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nom_rol VARCHAR(50) NOT NULL
);

-- Relación entre Usuarios y Roles
CREATE TABLE usuarios_roles (
    id_usr INT NOT NULL,
    id_rol INT NOT NULL,
    PRIMARY KEY (id_usr, id_rol),
    FOREIGN KEY (id_usr) REFERENCES usuarios(id_usr),
    FOREIGN KEY (id_rol) REFERENCES roles(id_rol)
);

-- Historial de Compras
CREATE TABLE historial_compras (
    id_historial INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    id_usr INT NOT NULL,
    id_producto INT NOT NULL,
    fecha_compra DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_usr) REFERENCES usuarios(id_usr),
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
);

-- Seguimiento de Pedidos
CREATE TABLE seguimiento_pedidos (
    id_seguimiento INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    id_pedido INT NOT NULL,
    estado_actual VARCHAR(50) NOT NULL,
    fecha_estado DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_pedido) REFERENCES pedidos(id_pedido)
);

