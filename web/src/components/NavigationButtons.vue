<template>
  <div class="navigation-buttons">
    <button
      :class="['nav-button', 'previous', 'secondary']"
      @click="$emit('previous')"
    >
      <svg viewBox="0 0 24 24" class="icon">
        <path d="M15.41 7.41L14 6l-6 6 6 6 1.41-1.41L10.83 12z"/>
      </svg>
      <span>Previous</span>
    </button>

    <button
      :class="['nav-button', 'next', 'primary']"
      @click="$emit('next')"
    >
      <span>Next</span>
      <svg viewBox="0 0 24 24" class="icon">
        <path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"/>
      </svg>
    </button>
  </div>
</template>

<script setup>
defineEmits(['previous', 'next'])
</script>

<style scoped>
.navigation-buttons {
  display: flex;
  gap: 1rem;
  align-items: center;
  justify-content: center;
}

.nav-button {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  border: none;
  border-radius: 12px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
  position: relative;
  overflow: hidden;
}

.nav-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
}

.nav-button:active {
  transform: translateY(0);
}

.icon {
  width: 20px;
  height: 20px;
  fill: currentColor;
}

.nav-button.primary {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
}

.nav-button.primary:hover:not(:disabled) {
  background: linear-gradient(135deg, #5a67d8 0%, #6b46c1 100%);
}

.nav-button.primary::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
  transition: left 0.5s;
}

.nav-button.primary:hover::before {
  left: 100%;
}

.nav-button.secondary {
  background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
  color: white;
}

.nav-button.secondary:hover:not(:disabled) {
  background: linear-gradient(135deg, #ec4899 0%, #ef4444 100%);
}

.nav-button.secondary::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
  transition: left 0.5s;
}

.nav-button.secondary:hover::before {
  left: 100%;
}

/* Button specific styles */
.nav-button.previous {
  flex-direction: row;
}

.nav-button.next {
  flex-direction: row;
}

@media (max-width: 640px) {
  .navigation-buttons {
    flex-direction: column;
    gap: 0.75rem;
  }

  .nav-button {
    width: 100%;
    justify-content: center;
  }
}
</style>