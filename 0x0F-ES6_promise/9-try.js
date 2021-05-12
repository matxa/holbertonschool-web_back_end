export default function guardrail(mathFunction) {
  const queue = [];
  try {
    queue.push(mathFunction());
  } catch (error) {
    const [err] = error.toString().split('\n');
    queue.push(err);
  } finally {
    queue.push('Guardrail was processed');
  }
  return queue;
}
