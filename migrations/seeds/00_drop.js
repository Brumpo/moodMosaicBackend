
exports.seed = function(knex, Promise) {
  // Deletes ALL existing entries
  return knex('dates').del()
    .then(() => knex('users').del())
}
