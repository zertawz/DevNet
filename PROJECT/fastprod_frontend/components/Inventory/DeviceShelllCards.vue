<template>
  <div>
    <v-row justify="center">
      <v-col lg="6" md="12" cols="12">
        <UiCard title="Show commands SHELL" icon="console" :flat="false">
          <template #content>
            <v-textarea
              outlined
              name="input-7-4"
              label="Show commands"
              v-model="showCommands"
            ></v-textarea>
            <div class="text-center">
              <v-btn
                outlined
                color="primary"
                @click="sendShowCommands"
                :loading="loadingShowCommands"
              >
                Send <v-icon>mdi-arrange-send-to-back</v-icon>
              </v-btn>
            </div>
          </template>
        </UiCard>
      </v-col>
      <v-col lg="6" md="12" cols="12">
        <UiCard title="Config commands SHELL" icon="console" :flat="false">
          <template #content>
            <v-textarea
              outlined
              name="input-7-4"
              label="Config commands"
              v-model="configCommands"
            ></v-textarea>
            <div class="text-center">
              <v-btn
                outlined
                color="primary"
                @click="sendConfigCommands"
                :loading="loadingConfigCommands"
              >
                Send <v-icon>mdi-arrange-send-to-back</v-icon>
              </v-btn>
                <v-alert
                  dense
                  text
                  type="success"
                  class="my-5"
                  v-if="!!configResult && !configError"
                >
                  Configuration deployed!
                </v-alert>
                <v-alert dense outlined type="error" class="my-5" v-if="configError">
                  Error config could not be deployed...
                </v-alert>
            </div>
          </template>
        </UiCard>
      </v-col>
      <v-col cols="12">
        <div v-if="!!result" class="text-center">
          <v-textarea
            :value="result"
            height="280"
            outlined
            color="primary"
            label="Output"
          ></v-textarea>
        </div>
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  data() {
    return {
      loadingShowCommands: false,
      selectedDeviceName: null,
      showCommands: null,
      configCommands: null,
      loadingConfigCommands: null,
      result: null,
      configResult: null,
      configError:false,
    };
  },
  mounted() {
    //this.getDevices();
    this.selectedDeviceName = this.$route.params.name;
  },
  methods: {
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
    sendShowCommands() {
      const data = { mode: "enable", commands: this.showCommands.split("\n") };
      this.loadingShowCommands = true;
      this.$store
        .dispatch("inventory/config", {
          name: this.$route.params.name,
          data: data,
        })
        .then((response) => {
          this.loadingShowCommands = false;
          this.result = response.data.result
            .map((item) => {
              return item.result;
            })
            .join("\n\n\n");
        })
        .catch((error) => {
          this.loadingShowCommands = false;
          console.log("error", error);
        });
    },
    sendConfigCommands() {
      const data = {
        mode: "config",
        commands: this.configCommands.split("\n"),
      };
      this.loadingConfigCommands = true;
      this.configError = false
      this.$store
        .dispatch("inventory/config", {
          name: this.$route.params.name,
          data: data,
        })
        .then((response) => {
          this.loadingConfigCommands = false;
          this.configResult = response.data.result;
        })
        .catch((error) => {
          this.configError = true
          this.loadingConfigCommands = false;
          console.log("error", error);
        });
    },
  },
};
</script>
