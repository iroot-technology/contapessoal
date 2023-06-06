create database contapessoal;
create role contapessoal ;
alter database contapessoal owner to contapessoal ;
\c contapessoal

create table stock (
    id serial primary key,
    symbol text,
    name text,
    currency text,
    website text
);

create table stock_price (
    id_stock serial primary key,
    price numeric(12,4),
    open numeric(12,4),
    low numeric(12,4),
    high numeric(12,4),
    bid numeric(12,4)
);

alter table stock_price add constraint stock_price_fkey foreign key (id_stock) references stock(id);

CREATE TYPE order_type AS ENUM ('B','S')

create table order (
    id serial primary key,
    id_stock integer,
    date date,
    quantity integer,
    price numeric(12,4),
    type order_type,
    created_at timestamp with time zone,
);

