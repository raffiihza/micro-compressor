import { Ai } from './vendor/@cloudflare/ai.js';

export default {
  async fetch(request, env) {
    const tasks = [];
    const ai = new Ai(env.AI);

    const url = new URL(request.url);
    const prompt = url.searchParams.get('prompt');

    if (!prompt) {
      return new Response("please fill prompt", {status: 400});
    }

    let simple = {
      prompt: prompt
    };
    let response = await ai.run('@cf/meta/llama-3-8b-instruct', simple);
    tasks.push({ inputs: simple, response });

    return Response.json(tasks);
  }
};
