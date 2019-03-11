-- drop table if exists user;
-- drop table if exists post;

create table if not exists user (
    id integer primary key autoincrement,
    username text unique not null,
    password text not null
);

create table if not exists wish (
    id integer primary key autoincrement,
    owner_id integer not null,
    created timestamp not null default current_timestamp,
    title text not null,
    content text not null,
    foreign key (owner_id) references user (id)
);