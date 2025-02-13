<!-- src/components/UsersComponent.vue -->
<template>
  <div>
    <el-button type="primary" @click="userDialog = true">添加用户</el-button>
    <el-table :data="users" style="width: 100%">
      <el-table-column prop="username" label="用户名" width="180"></el-table-column>
      <el-table-column prop="email" label="邮箱" width="180"></el-table-column>
      <el-table-column label="操作">
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
import { ref, onMounted } from 'vue';  // 修正导入路径
import axios from 'axios';
import { ElMessage } from 'element-plus';

export default {
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
        const response = await axios.get('/api/users/');
        users.value = response.data;
      } catch (error) {
        ElMessage.error('获取用户列表失败');
      }
    };

    const addUser = async () => {
      try {
        const response = await axios.post('/api/users/', newUser.value);
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
      }
    };

    const deleteUser = async (userId) => {
      try {
        await axios.delete(`/api/users/${userId}`);
        ElMessage.success('用户删除成功');
        users.value = users.value.filter(user => user.id !== userId);
      } catch (error) {
        ElMessage.error('用户删除失败');
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
</style>
