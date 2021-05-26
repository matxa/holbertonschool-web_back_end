import express from 'express';
import AppController from '../controllers/AppController';
import StudentsController from '../controllers/StudentsController';

const appRoutes = express.Router();
const studentRoutes = express.Router();

appRoutes.get('/', AppController.getHomepage);

studentRoutes.get('/', StudentsController.getAllStudents);
studentRoutes.get('/:major', StudentsController.getAllStudentsByMajor);

export { appRoutes, studentRoutes };
