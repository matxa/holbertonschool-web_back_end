import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  const photo = uploadPhoto();
  const user = createUser();
  return Promise.all([photo, user])
    .then((promises) => console.log(`${promises[0].body} ${promises[1].firstName} ${promises[1].lastName}`),
      () => console.log('Signup system offline'));
}
