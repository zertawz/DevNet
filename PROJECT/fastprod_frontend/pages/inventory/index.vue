<template>
  <div>
    <DialogBindComponent
      ref="addDeviceDialog"
      :header="dialogHeader"
      component="InventoryAddDeviceForm"
      @onSubmit="submitHandler"
    />

    <v-dialog v-model="dialog" persistent max-width="290">
      <v-card>
        <v-card-title class="text-center">
          Do you want to delete this device ?
        </v-card-title>
        <v-card-text v-if="!!selectedItem">
          Hostname : {{ selectedItem.data.device_name }}
          <br />
          Ip address :
          {{ selectedItem.hostname }}
          <br />
          Device type :
          {{ selectedItem.data.device_type }}
          <br />
          Device model :
          {{ selectedItem.data.device_model }}
          <br />
          <br />
          <span class="text-center error--text">
            Device will be permanently removed from the inventory
          </span>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="green darken-1" text @click="dialog = false">
            Cancel
          </v-btn>
          <v-btn color="error darken-1" text @click="deleteDevice">
            Delete
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-row justify="center" align="center">
      <v-col cols="12">
        <v-toolbar dense flat>
          <v-toolbar-title>
            <h3>Inventory</h3>
          </v-toolbar-title>
          <v-spacer></v-spacer>
          <v-tooltip bottom>
            <template #activator="{ on, attrs }">
              <v-btn
                color="primary"
                outlined
                v-bind="attrs"
                v-on="on"
                class="mr-2"
                @click="openDialog"
              >
                <v-icon>mdi-plus</v-icon>
              </v-btn>
            </template>
            <span> Add a new device </span>
          </v-tooltip>

          <v-tooltip bottom>
            <template #activator="{ on, attrs }">
              <v-btn
                v-bind="attrs"
                color="primary"
                outlined
                v-on="on"
                @click="getDevices"
              >
                <v-icon>mdi-refresh</v-icon>
              </v-btn>
            </template>
            <span> Refresh </span>
          </v-tooltip>
        </v-toolbar>
      </v-col>

      <v-col lg="10" md="10" cols="12">
        <UiCard title="Device list" icon="server" :flat="false">
          <template #headerActions>
            <v-progress-linear
              v-show="loading"
              color="primary"
              indeterminate
              rounded
              height="6"
            ></v-progress-linear>
          </template>
          <template #content>
            <InventoryTable :items="items" @onAction="handleAction" />
          </template>
        </UiCard>
      </v-col>
    </v-row>
    <v-snackbar v-model="snackbar" color="success">
      {{ notification.title }}
      <template v-slot:action="{ attrs }">
        <v-btn color="white" text v-bind="attrs" @click="snackbar = false">
          Close
        </v-btn>
      </template>
    </v-snackbar>
  </div>
</template>

<script>
export default {
  data() {
    return {
      notification: {},
      selectedItem: null,
      snackbar: false,
      loading: false,
      dialog: false,
      items: [],
      dialogHeader: {
        icon: "server",
        label: "Add a new device",
      },
    };
  },
  mounted() {
    this.getDevices();
  },
  methods: {
    getDevices() {
      this.loading = true;
      this.$store
        .dispatch("inventory/get")
        .then((response) => {
          this.loading = false;
          this.items = response.data.devices;
        })
        .catch((error) => {
          this.loading = false;
          console.log("error", error);
        });
    },
    openDialog() {
      this.$refs.addDeviceDialog.open();
    },
    submitHandler(e) {
      this.$refs.addDeviceDialog.close();
      this.notification.title = "Device added!";
      this.snackbar = true;
      this.getDevices();
    },
    handleAction(e) {
      console.log(e);
      if (e.action == "delete") {
        this.selectedItem = e.item;
        this.dialog = true;
      }
      if (e.action == "show") {
        this.$router.push({
          name: "inventory-name",
          params: { name: e.item.data.device_name },
        });
      }
    },
    deleteDevice() {
      this.dialog = false;
      this.loading = true;
      this.$store
        .dispatch("inventory/delete", {
          name: this.selectedItem.data.device_name,
        })
        .then((response) => {
          this.loading = false;
          this.notification.title = "Device removed!";
          this.snackbar = true;
          this.getDevices();
        })
        .catch((error) => {
          this.loading = false;
          console.log("error", error);
        });
    },
  },
};
</script>
