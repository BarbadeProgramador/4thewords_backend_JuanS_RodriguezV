
CREATE DATABASE 4thewords_prueba_juans_rodriguezv;

-- Crear tabla Categorias
CREATE TABLE Categorias (
    id INT PRIMARY KEY IDENTITY(1,1),
    nombre VARCHAR(255) NOT NULL
);

-- Crear tabla Provincias
CREATE TABLE Provincias (
    id INT PRIMARY KEY IDENTITY(1,1),
    nombre VARCHAR(255) NOT NULL
);

-- Crear tabla Canton
CREATE TABLE Canton (
    id INT PRIMARY KEY IDENTITY(1,1),
    nombre VARCHAR(255) NOT NULL
);

-- Crear tabla Distrito
CREATE TABLE Distrito (
    id INT PRIMARY KEY IDENTITY(1,1),
    nombre VARCHAR(255) NOT NULL
);

-- Crear tabla Leyendas
CREATE TABLE Leyendas (
    id INT PRIMARY KEY IDENTITY(1,1),
    nombre VARCHAR(255) NOT NULL,
    id_categoria INT NOT NULL,
    txt_descrip TEXT NOT NULL,
    fecha_leyenda DATE NOT NULL,
    id_provincia INT NOT NULL,
    id_canton INT NOT NULL,
    id_distrito INT NOT NULL,
    historia TEXT NOT NULL,
    imagen VARCHAR(255),
    FOREIGN KEY (id_categoria) REFERENCES Categorias(id),
    FOREIGN KEY (id_provincia) REFERENCES Provincias(id),
    FOREIGN KEY (id_canton) REFERENCES Canton(id),
    FOREIGN KEY (id_distrito) REFERENCES Distrito(id)
);

-- Insertar datos en Categorias
INSERT INTO Categorias (nombre) VALUES ('Mitos'), ('Historias de terror'), ('Leyendas populares');

-- Insertar datos en Provincias
INSERT INTO Provincias (nombre) VALUES ('San José'), ('Alajuela'), ('Cartago');

-- Insertar datos en Canton
INSERT INTO Canton (nombre) VALUES ('Central'), ('Grecia'), ('Turrialba');

-- Insertar datos en Distrito
INSERT INTO Distrito (nombre) VALUES ('Catedral'), ('San Roque'), ('Santa Cruz');

-- Insertar 10 registros en Leyendas
INSERT INTO Leyendas (nombre, id_categoria, txt_descrip, fecha_leyenda, id_provincia, id_canton, id_distrito, historia, imagen)
VALUES
    ('La Llorona', 2, 'Leyenda de una mujer que llora por sus hijos.', '1900-01-01', 1, 1, 1, 'Historia de la Llorona...', 'llorona.jpg'),
    ('El Cadejos', 1, 'Perro fantasmal que protege a los borrachos.', '1850-06-15', 2, 2, 2, 'Historia del Cadejos...', 'cadejos.jpg'),
    ('El Tule Viejo', 3, 'Árbol encantado donde aparecen espíritus.', '1923-10-20', 3, 3, 3, 'Historia del Tule Viejo...', 'tule_viejo.jpg'),
    ('La Segua', 2, 'Mujer que se convierte en bestia para asustar a los infieles.', '1875-03-12', 1, 1, 1, 'Historia de la Segua...', 'segua.jpg'),
    ('El Sombrerón', 1, 'Hombre pequeño que encanta a las mujeres con su música.', '1800-05-05', 2, 2, 2, 'Historia del Sombrerón...', 'sombreron.jpg'),
    ('El Duende', 3, 'Ser pequeño que asusta a los niños traviesos.', '1890-11-30', 3, 3, 3, 'Historia del Duende...', 'duende.jpg'),
    ('La Carreta sin Bueyes', 2, 'Carreta fantasmal que presagia la muerte.', '1910-07-07', 1, 1, 1, 'Historia de la Carreta...', 'carreta.jpg'),
    ('La Mona', 1, 'Mujer que se convierte en bestia y ataca a sus enemigos.', '1860-09-19', 2, 2, 2, 'Historia de la Mona...', 'mona.jpg'),
    ('El Zorro del Diablo', 3, 'Zorro que se dice es el demonio en persona.', '1950-02-22', 3, 3, 3, 'Historia del Zorro...', 'zorro.jpg'),
    ('La Tulevieja', 2, 'Espíritu de una madre que llora por su hijo perdido.', '1935-12-10', 1, 1, 1, 'Historia de la Tulevieja...', 'tulevieja.jpg');
