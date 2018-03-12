
exports.seed = function(knex, Promise) {
  // Deletes ALL existing entries
  return knex('users').insert([
    {
    id: 1,
    fname: 'sao',
    lname: 'sao',
    email: 'sao',
    password: '$2b$12$D.UkGKlBy72ZqNz853./1e4bZTsCl/bfNmS8zahoeUEoxPpYvVwHa',
    key1: 'feeling',
    key2: 'love',
    key3: 'religion',
    key4: 'preaching',
    key5: 'swearing',
    key6: 'flavor flute'
    },{
    id: 2,
    fname: 'Brent',
    lname: 'Schroder',
    email: 'schroder.brent@gmail.com',
    password: '$2b$12$FGQNmbaOgWle6CplOI1h4efvbPtOWJEJjgqMRHmrAWrdfvbVEvRDy'
    },{
    id: 3,
    fname: 'palo',
    lname: 'palo',
    email: 'palo',
    password: '$2b$12$dvNy2YQCeyy5I09.4S2KweL7l8d7KHK5EG7MJ4iZQ7XN7sc2Pu9Zm'
    },{
    id: 4,
    fname: 'sp',
    lname: 'sp',
    email: 'sp',
    password: '$2b$12$DNG5T1AeE3X2AYdo/4S5q.QsCw5W4ohBq9YbKOjzwMv1xOIC3GR4i'
    }
  ])
  .then(function(){
    return knex.raw("SELECT setval('users_id_seq', (SELECT MAX(id) FROM users))")
  })
};
