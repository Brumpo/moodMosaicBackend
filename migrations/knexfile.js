module.exports = {
  development: {
    client: 'pg',
    connection: 'postgres://localhost/moodmosaic'
  },

  production: {
    client: 'pg',
    connection: process.env.DATABASE_URL
  }
};
