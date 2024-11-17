<template>
  <UiCard title="Device informations" icon="server" :flat="false">
    <template #headerActions>
      <div class="text-center">
        <v-btn
          v-show="!loading"
          @click="$emit('refresh')"
          color="primary"
          outlined
        >
          Refresh
        </v-btn>
      </div>

      <div class="text-center" v-show="!loading">
        <v-icon size="100" color="primary">mdi-remote-desktop</v-icon>
        <br />
        <span class="text-h5 text-center" v-if="!!item">
          {{ item.hostname }}
        </span>
      </div>
    </template>
    <template #content>
      <div class="text-center">
        <v-progress-circular
          :size="70"
          :width="7"
          color="primary"
          indeterminate
          v-show="loading"
        ></v-progress-circular>
      </div>
      <v-divider class="mb-4" v-show="!loading"></v-divider>
      <v-row
        justify="center"
        align="center"
        class="text-center"
        v-if="!!item"
        v-show="!loading"
      >
        <v-col cols="12" class="text-capitalize">
          <v-icon color="primary"> mdi-webpack </v-icon>
          <span class="font-weight-bold">FQDN :</span>
          {{ item.fqdn }}
        </v-col>

        <v-col lg="4" md="4" cols="12">
          <v-icon color="primary"> mdi-office-building-cog-outline </v-icon>
          <span class="font-weight-bold">vendor :</span>
          {{ item.vendor }}
        </v-col>
        <v-col lg="4" md="4" cols="12">
          <v-icon color="primary"> mdi-cog-sync-outline </v-icon>
          <span class="font-weight-bold">Model :</span>
          {{ item.model }}
        </v-col>
        <v-col lg="4" md="4" cols="12">
          <v-icon color="primary"> mdi-barcode </v-icon>
          <span class="font-weight-bold">Serial number :</span>
          <span class="text-capitalize">
            {{ item.serial_number }}
          </span>
        </v-col>

        <v-col lg="4" md="4" cols="12">
          <v-icon color="primary"> mdi-clock-outline </v-icon>
          <span class="font-weight-bold">Up time :</span>
          <span class="text-capitalize">
            {{ item.uptime }}
          </span>
        </v-col>
        <v-col cols="12">
          <v-icon color="primary"> mdi-code-tags </v-icon>
          <span class="font-weight-bold">OS version :</span>
          <span class="text-capitalize">
            {{ item.os_version }}
          </span>
        </v-col>
      </v-row>
    </template>
  </UiCard>
</template>

<script>
export default {
  props: {
    item: {
      type: Object,
      default: null,
    },
    loading: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {};
  },
  mounted() {},
  methods: {},
};
</script>
<style scoped></style>
