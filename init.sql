CREATE TABLE Video (
    -- идентификатор видео
    ID INT PRIMARY KEY AUTO_INCREMENT,
    -- путь к файлу видео
    Path TEXT UNIQUE NOT NULL,
    -- описание видео
    Description TEXT DEFAULT '',
    -- текстовый образ видео
    Image TEXT NOT NULL
);
