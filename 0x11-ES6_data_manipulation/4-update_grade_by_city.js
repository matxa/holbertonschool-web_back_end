export default function updateStudentGradeByCity(getListStudents, city, newGrades) {
  return getListStudents.filter((currentValue) => currentValue.location === city)
    .map((currentValue) => {
      const obj = currentValue;
      for (const grade of newGrades) {
        if (grade.studentId === obj.id) {
          obj.grade = grade.grade;
        }
      }
      if (obj.grade === undefined) {
        obj.grade = 'N/A';
      }
      return obj;
    });
}
