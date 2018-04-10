
exports.up = function(knex, Promise) {
  return knex.schema.createTable('users', table => {
    table.increments('id')
    table.string('fname').notNullable()
    table.string('lname').notNullable()
    table.string('email').notNullable()
    table.unique('email')
    table.string('password').notNullable()
    table.string('key1').defaultsTo('Anxiety')
    table.string('key2').defaultsTo('Irritability')
    table.string('key3').defaultsTo('Mood')
    table.string('key4').defaultsTo('Sleep')
    table.string('key5').defaultsTo('Diet')
    table.string('key6').defaultsTo('Professional')
  })
};

exports.down = function(knex, Promise) {
  knex.schema.dropTable('users')
};
