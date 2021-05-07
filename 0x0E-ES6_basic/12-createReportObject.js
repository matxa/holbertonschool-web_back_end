export default function createReportObject(employeesList) {
  return {
    allEmployees: employeesList,
    getNumberOfDepartments(obj) {
      return Object.keys(obj).length;
    },
  };
}
