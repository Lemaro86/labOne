-- Use it from PG Admin tab: Query for postgres v.14

CREATE TABLE service
(
    service_id  SERIAL       NOT NULL PRIMARY KEY,
    title       VARCHAR(100) NOT NULL,
    description VARCHAR(255),
    cost        FLOAT(15)    NOT NULL,
    img         VARCHAR(50)  NOT NULL
);

CREATE TABLE public.user
(
    user_id  SERIAL NOT NULL PRIMARY KEY,
    login    VARCHAR(50),
    password VARCHAR(50),
    admin    BOOLEAN DEFAULT false
)

CREATE TABLE public.order
(
    order_id     SERIAL      NOT NULL PRIMARY KEY,
    status       VARCHAR(50) NOT NULL,
    created      TIMESTAMP   NOT NULL,
    moderator_id INTEGER,
    activated    TIMESTAMP,
    completed    TIMESTAMP,
    creator_id   INTEGER
)

CREATE TABLE public.order_event
(
    order_id   INTEGER,
    service_id INTEGER
)

ALTER TABLE public.order
    ADD CONSTRAINT moderator_id FOREIGN KEY (moderator_id) REFERENCES public.user (user_id);

ALTER TABLE public.order
    ADD CONSTRAINT creator_id FOREIGN KEY (creator_id) REFERENCES public.user (user_id);

ALTER TABLE public.order_event
    ADD CONSTRAINT order_id FOREIGN KEY (order_id) REFERENCES public.order (order_id);

ALTER TABLE public.order_event
    ADD CONSTRAINT service_id FOREIGN KEY (service_id) REFERENCES public.service (service_id);

INSERT INTO public.service (service_id, title, description, cost, img) VALUES(1, 'Обработка помещений после ковида', 'Дэзинфекция объектов', '50500', './img/1.png');
