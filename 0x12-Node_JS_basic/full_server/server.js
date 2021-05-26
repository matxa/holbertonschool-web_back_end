import express from 'express';
import { appRoutes, studentRoutes } from './routes/index';

const app = express();
app.use('/', appRoutes);
app.use('/students', studentRoutes);

const PORT = 1245;
app.listen(PORT, () => console.log(`Listening on PORT ${PORT} 🚀`));

export default app;
