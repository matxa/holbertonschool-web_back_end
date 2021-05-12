import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const outputList = [];
  const promise = Promise.allSettled([signUpUser(firstName, lastName), uploadPhoto(fileName)])
    .then((outputs) => {
      outputs.forEach((obj) => {
        const objCopy = obj;
        if (objCopy.status === 'rejected') {
          [objCopy.value] = objCopy.reason.toString().split('\n');
          delete objCopy.reason;
        }
        outputList.push(objCopy);
      });
      return outputList;
    });
  return promise;
}
