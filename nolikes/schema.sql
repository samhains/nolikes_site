drop table if exists images;
create table images (
  id integer primary key autoincrement,
  uuid text not null,
  file_url text not null,
  title text not null,
  caption text not null
);
