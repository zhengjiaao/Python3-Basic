<!-- example-frontend/frontend/src/views/Files.vue -->
<template>
  <div>
    <h1>Files</h1>
    <ul>
      <li v-for="file in files" :key="file.id">{{ file.filename }}</li>
    </ul>
    <input type="file" @change="uploadFile">
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      files: []
    }
  },
  async created() {
    const response = await axios.get('/files/')
    this.files = response.data
  },
  methods: {
    async uploadFile(event) {
      const file = event.target.files[0]
      const formData = new FormData()
      formData.append('file', file)
      await axios.post('/files/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })
      this.files = (await axios.get('/files/')).data
    }
  }
}
</script>
