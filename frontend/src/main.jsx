import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'
import './index.css'

import { createClient, configureChains, defaultChains, WagmiConfig } from 'wagmi';
import { publicProvider } from 'wagmi/providers/public';

const { provider, webSocketProvider } = configureChains(defaultChains, [publicProvider()]);

const client = createClient({
  provider,
  webSocketProvider,
  autoConnect: true,
});

ReactDOM.createRoot(document.getElementById('root')).render(
    <WagmiConfig client={client}>
      <App />
    </WagmiConfig>
)
