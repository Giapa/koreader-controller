<template>
  <div class="device-input">
    <form @submit.prevent="connectToDevice" class="input-form">
      <div class="input-group">
        <input
          v-model="deviceIP"
          type="text"
          placeholder="Enter device IP (e.g., 192.168.1.100)"
          class="ip-input"
          required
        />
        <button type="submit" class="connect-button">
          Connect
        </button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const deviceIP = ref('')

const emit = defineEmits(['deviceConnected'])

const connectToDevice = () => {
  if (deviceIP.value.trim()) {
    const device = { ip: deviceIP.value.trim() }
    emit('deviceConnected', device)
  }
}
</script>

<style scoped>
.device-input {
  margin: 2rem 0;
}

.input-form {
  width: 100%;
}

.input-group {
  display: flex;
  gap: 0.75rem;
  align-items: stretch;
}

.ip-input {
  flex: 1;
  padding: 1rem 1.5rem;
  border: 2px solid #e5e7eb;
  border-radius: 12px;
  font-size: 1rem;
  transition: all 0.3s ease;
  background: white;
}

.ip-input:focus {
  outline: none;
  border-color: #3b82f6;
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
}

.ip-input::placeholder {
  color: #9ca3af;
}

.connect-button {
  padding: 1rem 2rem;
  background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
  color: white;
  border: none;
  border-radius: 12px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  white-space: nowrap;
}

.connect-button:hover {
  background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
  transform: translateY(-1px);
}

@media (max-width: 640px) {
  .input-group {
    flex-direction: column;
    gap: 1rem;
  }
}
</style>