export default function uploadPhoto(fileName) {
  return Promise.reject(new Error(`Error: ${fileName} cannot be processed`));
}
