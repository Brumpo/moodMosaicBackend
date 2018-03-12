
exports.up = function(knex, Promise) {
  return knex.schema.createTable('dates', table => {
    table.increments('id')
    table.integer('day').notNullable()
    table.integer('year').notNullable()
    table.integer('userId').notNullable()
    table.foreign('userId').references('users.id')
    table.string('x1',3000)
    table.string('x2',3000)
    table.string('x3',3000)
    table.string('x4',3000)
    table.string('x5',3000)
    table.string('x6',3000)
    table.string('summary',3000)
    table.string('journal',3000)
  })
};

exports.down = function(knex, Promise) {

};
