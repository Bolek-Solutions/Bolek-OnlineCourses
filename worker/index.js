export default {
  async fetch(request, env) {
    const backendOrigin = env.BACKEND_ORIGIN;

    if (!backendOrigin) {
      return new Response('BACKEND_ORIGIN is not configured', { status: 500 });
    }

    const incomingUrl = new URL(request.url);
    const targetUrl = new URL(incomingUrl.pathname + incomingUrl.search, backendOrigin);

    const newHeaders = new Headers(request.headers);
    newHeaders.set('x-forwarded-host', incomingUrl.host);
    newHeaders.set('x-forwarded-proto', incomingUrl.protocol.replace(':', ''));

    const proxyRequest = new Request(targetUrl.toString(), {
      method: request.method,
      headers: newHeaders,
      body: request.method === 'GET' || request.method === 'HEAD' ? undefined : request.body,
      redirect: 'manual',
    });

    const response = await fetch(proxyRequest);
    const responseHeaders = new Headers(response.headers);
    responseHeaders.set('x-edge-proxy', 'cloudflare-worker');

    return new Response(response.body, {
      status: response.status,
      statusText: response.statusText,
      headers: responseHeaders,
    });
  },
};
