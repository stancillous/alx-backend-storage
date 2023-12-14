-- a SQL script that creates a trigger that decreases the quantity of an item after adding a new order.
CREATE TRIGGER decrease_quantity AFTER INSERT on orders
FOR EACH ROW
UPDATE ITEMS SET quantity = quantity - NEW.number WHERE name = NEW.item_name;
