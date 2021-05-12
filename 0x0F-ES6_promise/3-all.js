import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
    .then((output) => console.log(`${output[0].body} ${output[1].firstName} ${output[1].lastName}`),
      () => console.log('Signup system offline'));
}
