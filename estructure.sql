CREATE TABLE usuarios (
    id_usuario BIGINT primary key AUTOINCREMENT,
    tipo_usuario int not null,
    username varchar(50) unique not null,
    password_hash varchar(255) not null,
    fecha_creacion_usuario DATETIME not null,
    estado_usuario varchar(50) not null default activo,
    email_usuario varchar(255) not null default [example@example.com]
);

CREATE TABLE productos (
    id_producto BIGINT PRIMARY KEY AUTOINCREMENT,
    nombre_producto VARCHAR (50)  NOT NULL,
    codigo_producto VARCHAR (50)  UNIQUE NOT NULL,
    info_producto   VARCHAR (255) NOT NULL,
    precio_producto INT           NOT NULL,
    estado_producto VARCHAR (20)  NOT NULL DEFAULT active
);

CREATE TABLE ventas (
    id_venta bigint PRIMARY KEY AUTOINCREMENT,
    tipo_venta 
):