
exports.up = function(knex, Promise) {
  return knex.schema.createTable('users', table => {
    table.increments('id')
    table.string('fname').notNullable()
    table.string('lname').notNullable()
    table.string('email').notNullable()
    table.unique('email')
    table.string('password').notNullable()
    table.string('key1')
    table.string('key2')
    table.string('key3')
    table.string('key4')
    table.string('key5')
    table.string('key6')
  })
};

exports.down = function(knex, Promise) {
  knex.schema.dropTable('users')
};
