import getListStudentIds from './1-get_list_student_ids';

export default function getStudentIdsSum(getListStudents) {
  if (getListStudents instanceof Array) {
    return getListStudentIds(getListStudents).reduce((total, num) => total + num);
  }
  return 0;
}
