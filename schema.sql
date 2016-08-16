drop table if exists entries;
create table entries(
    id integer primary key autoincrement,
    title stirng not null,
    text string not null
);
