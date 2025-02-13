<!-- src/components/UsersComponent.vue -->
<template>
  <div>
    <el-button type="primary" @click="userDialog = true">添加用户</el-button>
    <el-table :data="users" style="width: 100%" fit>
      <el-table-column prop="username" label="用户名" min-width="150" max-width="200"></el-table-column>
      <el-table-column prop="email" label="邮箱" min-width="200" max-width="300"></el-table-column>
      <el-table-column label="操作" min-width="100" max-width="150">
        <template #default="scope">
          <el-button size="small" type="danger" @click="deleteUser(scope.row.id)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>

    <!-- 添加用户对话框 -->
    <el-dialog title="添加用户" v-model="userDialog" width="30%">
      <el-form :model="newUser" label-width="80px">
        <el-form-item label="用户名">
          <el-input v-model="newUser.username"></el-input>
        </el-form-item>
        <el-form-item label="邮箱">
          <el-input v-model="newUser.email"></el-input>
        </el-form-item>
        <el-form-item label="密码">
          <el-input v-model="newUser.password" type="password"></el-input>
        </el-form-item>
      </el-form>
      <template #footer>
        <span class="dialog-footer">
          <el-button @click="userDialog = false">取消</el-button>
          <el-button type="primary" @click="addUser">确定</el-button>
        </span>
      </template>
    </el-dialog>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import {
  ElMessage,
  ElButton,
  ElTable,
  ElTableColumn,
  ElDialog,
  ElForm,
  ElFormItem,
  ElInput
} from 'element-plus';

export default {
  components: {
    ElButton,
    ElTable,
    ElTableColumn,
    ElDialog,
    ElForm,
    ElFormItem,
    ElInput,
  },
  setup() {
    const users = ref([]);
    const userDialog = ref(false);
    const newUser = ref({
      username: '',
      email: '',
      password: '',
    });

    const fetchUsers = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/users/');
        console.log('Fetched users:', response.data); // 调试信息
        users.value = response.data;
      } catch (error) {
        ElMessage.error('获取用户列表失败');
        console.error('Error fetching users:', error); // 调试信息
      }
    };

    const addUser = async () => {
      try {
        const response = await axios.post('http://127.0.0.1:8000/api/users/', newUser.value);
        ElMessage.success('用户添加成功');
        users.value.push(response.data);
        userDialog.value = false;
        newUser.value = {
          username: '',
          email: '',
          password: '',
        };
      } catch (error) {
        ElMessage.error('用户添加失败');
        console.error('Error adding user:', error); // 调试信息
      }
    };

    const deleteUser = async (userId) => {
      try {
        await axios.delete(`http://127.0.0.1:8000/api/users/${userId}`);
        ElMessage.success('用户删除成功');
        users.value = users.value.filter(user => user.id !== userId);
      } catch (error) {
        ElMessage.error('用户删除失败');
        console.error('Error deleting user:', error); // 调试信息
      }
    };

    onMounted(() => {
      fetchUsers();
    });

    return {
      users,
      userDialog,
      newUser,
      addUser,
      deleteUser,
    };
  },
};
</script>

<style scoped>
.el-form-item {
  margin-bottom: 20px;
}

/* 响应式样式 */
@media (max-width: 768px) {
  .el-table-column {
    min-width: 100px !important;
    max-width: 150px !important;
  }
}
</style>
