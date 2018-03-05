
exports.up = function(knex, Promise) {
  return knex.schema.createTable('dates', table => {
    table.increments('id')
    table.integer('day').notNullable()
    table.integer('year').notNullable()
    table.integer('userId').notNullable()
    table.foreign('userId').references('users.id')
    table.string('atAGlance',3000)
    table.string('journal',3000)
  })
};

exports.down = function(knex, Promise) {

};
