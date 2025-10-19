import { StatusBar } from 'expo-status-bar';
import { useState } from 'react';
import {
  StyleSheet,
  Text,
  View,
  TextInput,
  TouchableOpacity,
  Alert,
} from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';

export default function App() {
  const [ipAddress, setIpAddress] = useState('');
  const [connectedIP, setConnectedIP] = useState(null);

  const handleConnect = () => {
    const trimmedIP = ipAddress.trim();
    if (!trimmedIP) {
      Alert.alert('Error', 'Please enter an IP address');
      return;
    }
    setConnectedIP(trimmedIP);
  };

  const handleDisconnect = () => {
    setConnectedIP(null);
    setIpAddress('');
  };

  const sendRequest = async (action) => {
    try {
      const url = `http://${connectedIP}:8080/${action}`;
      const response = await fetch(url, {
        method: 'GET',
        headers: {
          'Accept': 'application/json',
        },
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
    } catch (error) {
      Alert.alert(
        'Error',
        `Failed to send ${action} command. Make sure the KOReader HTTP server is running on port 8080.`
      );
      console.error('Request error:', error);
    }
  };

  if (connectedIP) {
    return (
      <SafeAreaView style={styles.container}>
        <StatusBar style="dark" />
        <View style={styles.content}>
          <Text style={styles.title}>KOReader Controller</Text>

          <TouchableOpacity
            style={[styles.button, styles.disconnectButton]}
            onPress={handleDisconnect}
          >
            <Text style={styles.buttonText}>Disconnect</Text>
          </TouchableOpacity>

          <View style={styles.connectedSection}>
            <Text style={styles.connectedText}>Connected to: {connectedIP}</Text>

            <View style={styles.controlButtons}>
              <TouchableOpacity
                style={[styles.button, styles.controlButton]}
                onPress={() => sendRequest('koreader/event/GotoViewRel/-1')}
              >
                <Text style={styles.buttonText}>{'<'} Previous Page</Text>
              </TouchableOpacity>

              <TouchableOpacity
                style={[styles.button, styles.controlButton]}
                onPress={() => sendRequest('koreader/event/GotoViewRel/1')}
              >
                <Text style={styles.buttonText}>Next Page {'>'}</Text>
              </TouchableOpacity>
            </View>
          </View>
        </View>
      </SafeAreaView>
    );
  }

  return (
    <SafeAreaView style={styles.container}>
      <StatusBar style="dark" />
      <View style={styles.content}>
        <Text style={styles.title}>KOReader Controller</Text>

        <Text style={styles.instructions}>
          Enter the IP address of your KOReader device
        </Text>

        <TextInput
          style={styles.input}
          placeholder="192.168.1.100"
          placeholderTextColor="#999"
          value={ipAddress}
          onChangeText={setIpAddress}
          keyboardType="numeric"
          autoCapitalize="none"
          autoCorrect={false}
        />

        <TouchableOpacity
          style={styles.button}
          onPress={handleConnect}
        >
          <Text style={styles.buttonText}>Connect</Text>
        </TouchableOpacity>

        <Text style={styles.helpText}>
          Make sure the KOReader HTTP server is running on port 8080
        </Text>
      </View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f5f5f5',
  },
  content: {
    flex: 1,
    padding: 20,
    justifyContent: 'center',
  },
  title: {
    padding: 28,
    fontSize: 28,
    fontWeight: 'bold',
    color: '#333',
    textAlign: 'center',
    marginBottom: 40,
  },
  instructions: {
    fontSize: 16,
    color: '#666',
    textAlign: 'center',
    marginBottom: 20,
  },
  input: {
    backgroundColor: '#fff',
    borderWidth: 1,
    borderColor: '#ddd',
    borderRadius: 12,
    padding: 16,
    fontSize: 18,
    color: '#333',
    marginBottom: 20,
    textAlign: 'center',
  },
  button: {
    backgroundColor: '#007AFF',
    borderRadius: 12,
    padding: 16,
    alignItems: 'center',
  },
  buttonText: {
    color: '#fff',
    fontSize: 18,
    fontWeight: '600',
  },
  helpText: {
    fontSize: 14,
    color: '#999',
    textAlign: 'center',
    marginTop: 20,
    fontStyle: 'italic',
  },
  disconnectButton: {
    backgroundColor: '#FF3B30',
    alignSelf: 'center',
    paddingHorizontal: 40,
    marginBottom: 40,
  },
  connectedSection: {
    flex: 1,
    justifyContent: 'center',
  },
  connectedText: {
    fontSize: 18,
    fontWeight: '600',
    color: '#333',
    textAlign: 'center',
    marginBottom: 40,
  },
  controlButtons: {
    flexDirection: 'row',
    gap: 16,
    justifyContent: 'center',
  },
  controlButton: {
    backgroundColor: '#34C759',
  },
});
