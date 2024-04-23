import { Ai } from './vendor/@cloudflare/ai.js';

export default {
  async fetch(request, env) {
    const tasks = [];
    const ai = new Ai(env.AI);

    // Extract the prompt from the request URL
    const url = new URL(request.url);
    const prompt = url.searchParams.get('prompt');

    if (!prompt) {
      return new Response("please fill prompt", {
        status: 400,
        headers: {
          'Access-Control-Allow-Origin': '*',
        },
      });
    }

    let simple = {
      prompt: prompt
    };
    let response = await ai.run('@cf/meta/llama-3-8b-instruct', simple);
    tasks.push({ inputs: simple, response });

    return new Response(JSON.stringify(tasks), {
      headers: {
        'Access-Control-Allow-Origin': '*',
      },
    });
  }
};
