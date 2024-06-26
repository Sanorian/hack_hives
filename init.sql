CREATE TABLE Video (
    -- идентификатор видео
    ID INT PRIMARY KEY AUTO_INCREMENT,
    -- путь к файлу видео
    URL TEXT UNIQUE NOT NULL,
    -- описание видео
    Description TEXT DEFAULT '',
    -- текстовый образ видео
    Image TEXT NOT NULL,
    -- дата загрузки
    Upload_date timestamp not null default CURRENT_TIMESTAMP
);
