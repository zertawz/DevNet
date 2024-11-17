<template>
  <UiCard title="Configured interfaces" icon="connection" :flat="false">
    <template #headerActions>
      <div class="text-center">
        <v-btn
          @click="$emit('refresh')"
          color="primary"
          outlined
          v-show="!loading"
        >
          Refresh
        </v-btn>
      </div>
      <div class="text-center" v-show="!loading">
        <v-icon size="100" color="primary">mdi-connection</v-icon>
        <br />
        <span class="text-h5 text-center" v-if="!!items">
          {{ deviceName }}
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

      <div v-if="!!items" v-show="!loading">
        <v-row justify="end">
          <v-col cols="4">
            <v-text-field
              v-if="items.length > 1"
              v-model="search"
              color="secondary"
              append-icon="mdi-magnify"
              label="search an interface..."
              single-line
              hide-details
            ></v-text-field>
          </v-col>
        </v-row>
        <v-data-table
          hide-default-footer
          class="row-pointer"
          :search="search"
          :headers="headers"
          :items="items"
          :items-per-page="100"
        >
        </v-data-table>
      </div>
    </template>
  </UiCard>
</template>

<script>
export default {
  props: {
    items: {
      type: Array,
      default: null,
    },
    loading: {
      type: Boolean,
      default: false,
    },
    deviceName: {
      type: String,
      default: false,
    },
  },
  data() {
    return {
      search:"",
      headers: [
        {
          text: "Name",
          value: "name",
          align: "center",
        },
        {
          text: "Ip address",
          value: "ip",
          align: "center",
        },
        {
          text: "Prefix length",
          value: "prefix_length",
          align: "center",
        },
      ],
    };
  },
  mounted() {},
  methods: {},
};
</script>
<style scoped></style>
