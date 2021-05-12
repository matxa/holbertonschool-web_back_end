import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  const uPhoto = uploadPhoto();
  const cUser = createUser();
  Promise.all([uPhoto, cUser])
    .then((output) => console.log(`${output[0].body} ${output[1].firstName} ${output[1].lastName}`),
      () => console.log('Signup system offline'));
}
