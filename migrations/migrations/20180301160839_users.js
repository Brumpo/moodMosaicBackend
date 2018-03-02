
exports.up = function(knex, Promise) {
  return knex.schema.createTable('users', table => {
    table.increments('id')
    table.string('fname').notNullable()
    table.string('lname').notNullable()
    table.string('email').notNullable()
    table.string('password').notNullable()
  })
};

exports.down = function(knex, Promise) {
  knex.schema.dropTable('users')
};
