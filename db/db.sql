create database contapessoal;
create role contapessoal login;
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
    bid numeric(12,4),
    ask numeric(12,4)
);

alter table stock_price add constraint stock_price_fkey foreign key (id_stock) references stock(id);

CREATE TYPE order_type AS ENUM ('B','S');

create table orders (
    id serial primary key,
    id_stock integer,
    date date default current_date,
    quantity integer,
    price numeric(12,4),
    type order_type,
    created_at timestamp with time zone
);

alter table stock owner to contapessoal ;
alter table stock_price owner to contapessoal ;
alter table orders owner to contapessoal ;

with stock as(
    select * from stock s join stock_price sp on (s.id = sp.id_stock) where s.id = 20
), q as (
select 
    s.id as id, 
    sum(quantity) as qtde,
    sum(quantity*o.price) as total,
    round(sum(quantity*o.price)/sum(quantity),2) as pm
  from orders o 
  join stock s on (o.id_stock=s.id) 
 --where o.id_stock=20 
 group by s.id
)
select 
    q.id,
    stock.symbol,
    q.qtde,
    q.total AS total_investido,
    q.qtde * stock.price as total_mercado,
    round(q.pm, 2) AS preco_medio,
    round(stock.price,2) AS preco_mercado,
    q.qtde * stock.price - q.total AS saldo
    from stock join q using (id)
;


# Restart
truncate stock cascade ;
alter sequence stock_id_seq restart ;
