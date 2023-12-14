resources:
<h5>Triggers</h5>
Triggers in mysql are used to set automatic actions that should happen every time a specific event occurs (eg. BEFORE INSERT, AFTER DELETE, BEFORE UPDATE, AFTER INSERT etc) 
read -> https://www.digitalocean.com/community/tutorials/how-to-use-triggers-in-mysql

<h5>Stored procedures</h5>
Help reducing writing the same sql syntax over and over. If there's a syntax that you're sure you or users will be using in your database e.g
`SELECT * FROM cars WHERE year_make=2000 ORDER BY value DESC;`
Instead of writing that long sentence every time you want to run it, you can simply create a procedure for it.
read -> https://www.digitalocean.com/community/tutorials/how-to-use-stored-procedures-in-mysql


<h5>Views</h5>
In SQL, a view is a virtual table whose contents are the result of a specific query to one or more tables, known as base tables
read more -> https://www.digitalocean.com/community/tutorials/how-to-use-views-in-sql