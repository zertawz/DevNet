<template>
  <div>
    <DialogBindComponent
      ref="deviceShell"
      :header="dialogHeader"
      component="InventoryDeviceShelllCards"
      @onSubmit="submitHandler"
      :width="'1800'"
    />
    <v-row justify="center">
      <v-col cols="12">
        <v-toolbar dense flat>
          <v-toolbar-title>
            <h3>{{ selectedDeviceName }}</h3>
          </v-toolbar-title>
          <v-spacer></v-spacer>
          <v-tooltip bottom>
            <template #activator="{ on, attrs }">
              <v-btn
                v-bind="attrs"
                color="primary"
                class="mr-2"
                outlined
                v-on="on"
                @click="showShellDialog"
              >
                <v-icon>mdi-console</v-icon>
              </v-btn>
            </template>
            <span> Console </span>
          </v-tooltip>
          <v-tooltip bottom>
            <template #activator="{ on, attrs }">
              <v-btn
                v-bind="attrs"
                color="primary"
                outlined
                v-on="on"
                @click="refreshAll"
              >
                <v-icon>mdi-refresh</v-icon>
              </v-btn>
            </template>
            <span> Refresh </span>
          </v-tooltip>
        </v-toolbar>
      </v-col>
      <v-col lg="6" md="10" cols="12">
        <InventoryDeviceInfoCard
          :loading="loading"
          :item="device"
          :device-name="selectedDeviceName"
        />

        <InventoryDeviceFactsCard
          :item="deviceFacts"
          :loading="loadingFacts"
          @refresh="getDeviceFacts"
        />
      </v-col>

      <v-col lg="6" md="10" cols="12">
        <InventoryDeviceSanpshotsCard
          :items="deviceSnapshots"
          :loading="loadingSnapshots"
          @refresh="getDeviceSnapshots"
          @createSnapshot="buildSnapshot"
          :device-name="selectedDeviceName"
        />
      </v-col>

      <v-col lg="6" md="10" cols="12">
        <InventoryDeviceIpInterfacesCard
          :items="deviceIpInterfaces"
          :device-name="selectedDeviceName"
          :loading="loadingIpInterfaces"
          @refresh="getdeviceIpInterfaces"
        />
      </v-col>
      <v-col lg="6" md="10" cols="12">
        <InventoryDeviceInterfacesCard
          :items="deviceInterfaces"
          :device-name="selectedDeviceName"
          :loading="loadingInterfaces"
          @refresh="getdeviceInterfaces"
        />
      </v-col>
    </v-row>
    <v-snackbar v-model="snackbar" color="success" class="font-weight-bold">
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
      loading: false,
      loadingFacts: false,
      loadingIpInterfaces: false,
      loadingInterfaces: false,
      loadingSnapshots: false,
      notification: {},
      selectedDeviceName: null,
      device: null,
      deviceFacts: null,
      deviceInterfaces: null,
      deviceIpInterfaces: null,
      deviceSnapshots: null,
      snackbar: false,
      dialog: false,
      items: [],
      dialogHeader: {
        icon: "console",
        label: "FastProd SHELL",
      },
    };
  },
  mounted() {
    //this.getDevices();
    this.selectedDeviceName = this.$route.params.name;
    this.getDeviceByName();
    this.getDeviceFacts();
    this.getdeviceIpInterfaces();
    this.getdeviceInterfaces();
    this.getDeviceSnapshots();
  },
  methods: {
    refreshAll() {
      this.getDeviceByName();
      this.getDeviceFacts();
      this.getdeviceIpInterfaces();
      this.getdeviceInterfaces();
      this.getDeviceSnapshots();
    },
    getDeviceByName() {
      this.loading = true;
      this.$store
        .dispatch("inventory/getByName", { name: this.$route.params.name })
        .then((response) => {
          this.loading = false;
          this.device = response.data.device;
        })
        .catch((error) => {
          this.loading = false;
          console.log("error", error);
        });
    },
    getDeviceFacts() {
      this.loadingFacts = true;
      this.$store
        .dispatch("inventory/getFacts", { name: this.$route.params.name })
        .then((response) => {
          this.loadingFacts = false;
          this.deviceFacts = response.data.facts;
        })
        .catch((error) => {
          this.loadingFacts = false;
          console.log("error", error);
        });
    },
    getdeviceIpInterfaces() {
      this.loadingIpInterfaces = true;
      this.$store
        .dispatch("inventory/getInterfacesIp", {
          name: this.$route.params.name,
        })
        .then((response) => {
          this.loadingIpInterfaces = false;
          this.deviceIpInterfaces = response.data.interfaces_ip;
        })
        .catch((error) => {
          this.loadingIpInterfaces = false;
          console.log("error", error);
        });
    },
    getdeviceInterfaces() {
      this.loadingInterfaces = true;
      this.$store
        .dispatch("inventory/getInterfaces", {
          name: this.$route.params.name,
        })
        .then((response) => {
          this.loadingInterfaces = false;
          this.deviceInterfaces = response.data.interfaces;
        })
        .catch((error) => {
          this.loadingInterfaces = false;
          console.log("error", error);
        });
    },
    getDeviceSnapshots() {
      this.loadingSnapshots = true;
      this.$store
        .dispatch("inventory/getSnapshots", {
          name: this.$route.params.name,
        })
        .then((response) => {
          this.loadingSnapshots = false;
          this.deviceSnapshots = response.data.snapshots;
        })
        .catch((error) => {
          this.loadingSnapshots = false;
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
    buildSnapshot() {
      this.$store
        .dispatch("inventory/buildSnapshots", {
          name: this.$route.params.name,
        })
        .then((response) => {
          this.notification.title = "Snapshot created!";
          this.snackbar = true;
          this.getDeviceSnapshots();
        })
        .catch((error) => {
          console.log("error", error);
        });
    },

    showShellDialog() {
      this.$refs.deviceShell.open();
    },
  },
};
</script>
