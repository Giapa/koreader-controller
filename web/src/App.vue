<script setup>
import { ref } from 'vue'
import NavigationButtons from './components/NavigationButtons.vue'
import DeviceInput from './components/DeviceInput.vue'

const connectedDevice = ref(null)

const handlePrevious = () => {
  if (connectedDevice.value) {
    fetch(`http://${connectedDevice.value.ip}:8080/koreader/event/GotoViewRel/-1`, { method: 'GET' })
      .catch(err => console.log('Navigation request failed:', err))
  }
}

const handleNext = () => {
  if (connectedDevice.value) {
    fetch(`http://${connectedDevice.value.ip}:8080/koreader/event/GotoViewRel/1`, { method: 'GET' })
      .catch(err => console.log('Navigation request failed:', err))
  }
}

const handleDeviceConnected = (device) => {
  connectedDevice.value = device
}
</script>

<template>
  <div class="app-container">
    <div class="main-wrapper">
      <div class="instructions-text">
        Open koreader → settings → go to second page → more tools → KOReader HTTP inspector → Start HTTP server
      </div>

      <DeviceInput @device-connected="handleDeviceConnected" />
        <NavigationButtons
          v-if="connectedDevice"
          @previous="handlePrevious"
          @next="handleNext"
        />
    </div>
  </div>
</template>

<style scoped>
.app-container {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
  padding: 2rem;
}

.main-wrapper {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(10px);
  border-radius: 24px;
  padding: 3rem;
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.15);
  text-align: center;
  max-width: 600px;
  width: 100%;
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.instructions-text {
  font-size: 1.1rem;
  color: #374151;
  margin-bottom: 2rem;
  line-height: 1.6;
  background: linear-gradient(135deg, #e0e7ff 0%, #f3f4f6 100%);
  padding: 1.5rem;
  border-radius: 16px;
  border-left: 4px solid #6366f1;
  font-weight: 500;
}

.connection-status {
  background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%);
  color: #065f46;
  padding: 1rem 1.5rem;
  border-radius: 12px;
  border: 1px solid #10b981;
  font-weight: 600;
  font-size: 1rem;
  box-shadow: 0 4px 6px -1px rgba(16, 185, 129, 0.1);
}

.theme-toggle {
  margin-top: 2rem;
  padding: 0.5rem 1rem;
  background: transparent;
  border: 2px solid #6b7280;
  border-radius: 8px;
  color: #6b7280;
  cursor: pointer;
  transition: all 0.3s ease;
  font-size: 0.9rem;
}

.theme-toggle:hover {
  background: #6b7280;
  color: white;
  transform: translateY(-1px);
}

@media (max-width: 640px) {
  .app-container {
    padding: 1rem;
  }

  .main-wrapper {
    padding: 2rem;
  }

  .instructions-text {
    font-size: 1rem;
    padding: 1rem;
  }
}
</style>
