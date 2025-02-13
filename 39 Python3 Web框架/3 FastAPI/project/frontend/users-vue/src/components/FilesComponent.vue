<template>
  <div>
    <el-button type="primary" @click="uploadFileDialog = true">上传文件</el-button>
    <el-table :data="files" style="width: 100%">
      <el-table-column prop="filename" label="文件名" width="180"></el-table-column>
      <el-table-column prop="file_id" label="ID" width="180"></el-table-column>
      <el-table-column label="操作">
        <template #default="scope">
          <el-button size="small" @click="previewFile(scope.row.file_id)">预览</el-button>
          <el-button size="small" type="danger" @click="deleteFile(scope.row.file_id)">删除
          </el-button>
        </template>
      </el-table-column>
    </el-table>

    <!-- 上传文件对话框 -->
    <el-dialog title="上传文件" v-model="uploadFileDialog" width="30%">
      <el-upload
        class="upload-demo"
        action="http://127.0.0.1:8000/api/files/"
        :on-success="handleUploadSuccess"
        :before-upload="beforeUpload"
        :auto-upload="true"
        :show-file-list="false"
      >
        <el-button slot="trigger" type="primary">选取文件</el-button>
        <el-button type="success" @click="submitUpload">上传到服务器</el-button>
      </el-upload>
    </el-dialog>
  </div>
</template>

<script>
import {ref, onMounted} from 'vue';
import axios from 'axios';
import {ElMessage} from 'element-plus';
import {ElUpload, ElButton, ElTable, ElTableColumn, ElDialog} from 'element-plus';

export default {
  components: {
    ElUpload,
    ElButton,
    ElTable,
    ElTableColumn,
    ElDialog,
  },
  setup() {
    const files = ref([]);
    const uploadFileDialog = ref(false);

    const fetchFiles = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/files/');
        files.value = response.data;
      } catch (error) {
        ElMessage.error('获取文件列表失败');
      }
    };

    const handleUploadSuccess = (response, file, fileList) => {
      ElMessage.success('文件上传成功');
      fetchFiles();
      uploadFileDialog.value = false;
    };

    const beforeUpload = (file) => {
      // 你可以在这里添加文件上传前的验证逻辑
      return true;
    };

    const submitUpload = () => {
      // 上传文件的逻辑已经在 el-upload 组件中处理
    };

    const previewFile = async (fileId) => {
      try {
        // const response = await axios.get(`http://127.0.0.1:8000/api/files/${fileId}/preview`, {
        //   responseType: 'blob',
        // });
        // const url = window.URL.createObjectURL(new Blob([response.data]));

        const url = 'http://127.0.0.1:8000/api/files/' + fileId + '/preview'

        window.open(url, '_blank');
      } catch (error) {
        ElMessage.error('预览文件失败');
      }
    };

    const deleteFile = async (fileId) => {
      try {
        await axios.delete(`http://127.0.0.1:8000/api/files/${fileId}`);
        ElMessage.success('文件删除成功');
        fetchFiles();
      } catch (error) {
        ElMessage.error('删除文件失败');
      }
    };

    onMounted(() => {
      fetchFiles();
    });

    return {
      files,
      uploadFileDialog,
      handleUploadSuccess,
      beforeUpload,
      submitUpload,
      previewFile,
      deleteFile,
    };
  },
};
</script>

<style scoped>
.upload-demo {
  text-align: center;
}
</style>
